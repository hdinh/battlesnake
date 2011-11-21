import threading
import board
from board import Board
from PySide import QtCore, QtGui
from Queue import Queue


SnakeColors = {
    board.Snake_None: QtGui.QColor(0x000000),
    board.Snake_P1:   QtGui.QColor(0xff0000),
    board.Snake_P2:   QtGui.QColor(0x00ff00),
    board.Snake_P3:   QtGui.QColor(0x0000ff),
    board.Snake_P4:   QtGui.QColor(0x00ffff)
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

        self.setWindowTitle('Battle Snake')
        self.resize(Board.BOARD_WIDTH * QtSnakeWindow.BLOCK_WIDTH,
                    Board.BOARD_HEIGHT * QtSnakeWindow.BLOCK_HEIGHT)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000 / 20, self)

    def paintEvent(self, event):
        super(QtSnakeWindow, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        rect = self.contentsRect()

        for i in range(Board.BOARD_WIDTH):
            for j in range(Board.BOARD_HEIGHT):
                #import pdb; pdb.set_trace()
                piece = self.board.get_object_at(i, j)
                if piece is not None:
                    #print('...drawing...')
                    #color = SnakeColors[piece]
                    color = QtGui.QColor(0x000000)
                    if hasattr(piece, 'color'):
                        color = piece.color
                    self.drawTail(painter, i, j, color, None)

    def timerEvent(self, event):
        super(QtSnakeWindow, self).timerEvent(event)

        # Hack?
        self.repaint()

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
        painter.fillRect(x * QtSnakeWindow.BLOCK_WIDTH,
                         y * QtSnakeWindow.BLOCK_HEIGHT,
                         QtSnakeWindow.BLOCK_WIDTH,
                         QtSnakeWindow.BLOCK_HEIGHT,
                         color)
        painter.setPen(color.darker())


class QtBoard(Board):
    def __init__(self, board_actor):
        Board.__init__(self, board_actor)

        self.inc_x, self.inc_y, self.dec_x, self.dec_y = [False] * 4

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
        pass

    def putKey(self, direction):
        self.key_buffer.put(direction)

    def getKey(self):
        try:
            return self.key_buffer.get_nowait()
        except:
            return None
