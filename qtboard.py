import threading
import board
from board import Board
from PySide import QtCore, QtGui
from Queue import Queue


SnakeColors = {
    board.Snake_None: 0x000000,
    board.Snake_P1:   0xff0000,
    board.Snake_P2:   0x00ff00,
    board.Snake_P3:   0x0000ff,
    board.Snake_P4:   0x00ffff
}


class QtGuiThread(threading.Thread):
    def __init__(self, board):
        threading.Thread.__init__(self)
        self.board = board

    def run(self):
        self.app = QtGui.QApplication([])
        self.window = QtSnakeWindow(self.board)
        self.window.show()
        self.app.exec_()


class QtSnakeWindow(QtGui.QWidget):
    BLOCK_WIDTH = 12
    BLOCK_HEIGHT = 12

    def __init__(self, board):
        super(QtSnakeWindow, self).__init__()

        self.board = board

        self.setWindowTitle('Snake')
        self.resize(Board.BOARD_WIDTH * QtSnakeWindow.BLOCK_WIDTH,
                    Board.BOARD_HEIGHT * QtSnakeWindow.BLOCK_HEIGHT)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(10, self)

    def paintEvent(self, event):
        super(QtSnakeWindow, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        rect = self.contentsRect()

        for i in range(Board.BOARD_WIDTH):
            for j in range(Board.BOARD_HEIGHT):
                piece = self.board.board[(i * Board.BOARD_HEIGHT) + j]
                if piece is not board.Snake_None:
                    print('...drawing...')
                    color = QtGui.QColor(SnakeColors[piece])
                    self.drawTail(painter, i, j, color, None)

    def timerEvent(self, event):
        super(QtSnakeWindow, self).timerEvent(event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Left:
            self.board.putKey(board.Snake_GoLeft)
        elif key == QtCore.Qt.Key_Right:
            self.board.putKey(board.Snake_GoRight)
        elif key == QtCore.Qt.Key_Down:
            self.board.putKey(board.Snake_GoDown)
        elif key == QtCore.Qt.Key_Up:
            self.board.putKey(board.Snake_GoUp)
        else:
            super(QtSnakeWindow, self).keyPressEvent(event)

    def drawTail(self, painter, x, y, color, shape):
        painter.fillRect(x,
                         y,
                         QtSnakeWindow.BLOCK_WIDTH,
                         QtSnakeWindow.BLOCK_HEIGHT,
                         color)
        painter.setPen(color.darker())


class QtBoard(Board):
    def __init__(self):
        Board.__init__(self)
        self.inc_x, self.inc_y, self.dec_x, self.dec_y = [False] * 4
        self.x = 10
        self.y = 10

    def init(self):
        self.key_buffer = Queue(10)

    def finish(self):
        pass

    def init_game(self):
        self.thread = QtGuiThread(self)
        self.thread.start()

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        self.handle_turn()
        self.board[(self.x * Board.BOARD_WIDTH) + self.y] = board.Snake_None
        if self.dec_x:
            self.x = self.x - 1
        elif self.inc_x:
            self.x = self.x + 1
        elif self.inc_y:
            self.x = self.y + 1
        elif self.dec_y:
            self.x = self.y - 1
        self.board[(self.x * Board.BOARD_WIDTH) + self.y] = board.Snake_P1
        print("(%s, %s)" % (self.x, self.y))

    def handle_turn(self):
        self.inc_x, self.inc_y, self.dec_x, self.dec_y = [False] * 4
        key = self.getKey()
        if key != None:
            if key == board.Snake_GoLeft:
                self.dec_x = True
            elif key == board.Snake_GoRight:
                self.inc_x = True
            elif key == board.Snake_GoUp:
                self.inc_y = True
            elif key == board.Snake_GoDown:
                self.dec_y = True

    def putKey(self, direction):
        self.key_buffer.put(direction)

    def getKey(self):
        try:
            return self.key_buffer.get_nowait()
        except:
            return None
