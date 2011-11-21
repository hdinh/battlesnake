from PySide import QtCore, QtGui
from game_actor import GameActor
import board


class Snake(GameActor):
    def __init__(self, global_actor, board):
        GameActor.__init__(self, global_actor)
        self.board = board

    def init(self):
        pass

    def finish(self):
        pass

    def init_game(self):
        self.snake = self.new_object()
        self.snake.x = 0
        self.snake.y = 0
        self.snake.color = QtGui.QColor(0xff0000)

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        self.handle_turn()
        #self.board[(self.x * Board.BOARD_HEIGHT) + self.y] = board.Snake_None
        if self.dec_x:
            self.snake.x -= 1
        elif self.inc_x:
            self.snake.x += 1
        elif self.inc_y:
            self.snake.y += 1
        elif self.dec_y:
            self.snake.y -= 1
        #self.board[(self.x * Board.BOARD_HEIGHT) + self.y] = board.Snake_P1
        #print("(%s, %s)" % (self.x, self.y))

    def handle_turn(self):
        self.inc_x, self.inc_y, self.dec_x, self.dec_y = [False] * 4
        key = self.board.getKey()
        if key != None:
            if key == board.Snake_GoLeft:
                self.dec_x = True
            elif key == board.Snake_GoRight:
                self.inc_x = True
            elif key == board.Snake_GoUp:
                self.dec_y = True
            elif key == board.Snake_GoDown:
                self.inc_y = True
