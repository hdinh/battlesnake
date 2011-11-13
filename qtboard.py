import threading
from board import Board
from PySide import QtCore, QtGui


class QtGuiThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.app = QtGui.QApplication([])
        self.window = QtSnakeWindow()
        self.window.show()
        self.app.exec_()


class QtSnakeWindow(QtGui.QWidget):
    def __init__(self):
        super(QtSnakeWindow, self).__init__()

        self.setWindowTitle('Snake')
        self.resize(550, 550)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000, self)

    def paintEvent(self, event):
        super(QtSnakeWindow, self).paintEvent(event)

        painter = QtGui.QPainter(self)
        rect = self.contentsRect()
        #self.painter.drawText(rect, QtCore.Qt.AlignCenter, "Fart")

        for i in range(Board.BOARDWIDTH):
            for j in range(Board.BOARDHEIGHT):
                self.drawTail(painter, 20, 20, None)

    def timerEvent(self, event):
        pass

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Left:
            pass
        elif key == QtCore.Qt.Key_Right:
            pass
        elif key == QtCore.Qt.Key_Down:
            pass
        elif key == QtCore.Qt.Key_Up:
            pass
        else:
            super(QtSnakeWindow, self).keyPressEvent(event)

    def drawTail(self, painter, x, y, shape):
        color = QtGui.QColor(0xFF0000)
        painter.fillRect(x + 1, y + 1, 10, 10, color)
        painter.setPen(color.darker())
        #painter.drawLine(x, y, 2, 2, color)


class QtBoard(Board):
    def __init__(self):
        Board.__init__(self)

    def init(self):
        print('init')

    def finish(self):
        pass

    def init_game(self):
        self.thread = QtGuiThread()
        self.thread.start()

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        print('tick')
        pass

