import random
from game_actor import GameActor
from board import Board
import game_types


class Mushroom(GameActor):
    TICK_FREQ = 20
    MAX_MUSHROOMS = 10

    def __init__(self, global_actor):
        GameActor.__init__(self, global_actor)

        self.current_tick = 0
        self.num_mushrooms = 0

    def init(self):
        pass

    def finish(self):
        pass

    def init_game(self):
        pass

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        self.current_tick += 1
        if self.current_tick < Mushroom.TICK_FREQ:
            return

        self.current_tick = 0
        under_max = self.num_mushrooms < Mushroom.MAX_MUSHROOMS
        if under_max and random.random() < .1:
            self.num_mushrooms += 1
            self._activate_mushroom()

    def _activate_mushroom(self):
        obj = self.new_object()
        obj.x = random.randint(0, Board.BOARD_WIDTH)
        obj.y = random.randint(0, Board.BOARD_HEIGHT)
        obj.type = game_types.Mushroom
        self.activate_object(obj)
