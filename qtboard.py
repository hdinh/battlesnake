import threading
from board import Board
from PySide import QtCore, QtGui


class QtGuiThread(threading.Thread):
    def __init__(self):
        #self.app = app
        threading.Thread.__init__(self)

    def run(self):
        self.app = QtGui.QApplication([])
        self.window = QtSnakeWindow()
        self.window.show()
        self.app.exec_()


class QtSnakeWindow(QtGui.QWidget):
    pass


class QtBoard(Board):
    def __init__(self):
        Board.__init__(self)

    def init(self):
        print('tick')

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

