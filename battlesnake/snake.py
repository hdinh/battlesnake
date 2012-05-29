from game_actor import GameActor
import board
from fruit import Fruit
import game_types


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
        self.snake.type = game_types.Snake
        self.snake.color = 0xff0000

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        self.handle_turn()
        next_x = self.snake.x
        next_y = self.snake.y
        if self.dec_x:
            next_x -= 1
        elif self.inc_x:
            next_x += 1
        elif self.inc_y:
            next_y += 1
        elif self.dec_y:
            next_y -= 1

        obj = self.board.get_object_at(next_x, next_y)
        if obj and obj.type == game_types.Fruit:
            self.deactivate(obj)

        self.snake.x = next_x
        self.snake.y = next_y

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
