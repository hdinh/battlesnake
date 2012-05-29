from game_actor import GameActor
import random
from game_actor import GameActor
from board import Board
import game_types


class HeadBanger(GameActor):
    TICK_FREQ = 30
    MAX_HEADBANGERS = 1

    def __init__(self, global_actor):
        GameActor.__init__(self, global_actor)

        self.current_tick = 0
        self.num_headbangers = 0

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
        if self.current_tick < HeadBanger.TICK_FREQ:
            return

        self.current_tick = 0
        if self.num_headbangers < HeadBanger.MAX_HEADBANGERS and random.random() < .1:
            self.num_headbangers += 1
            self._activate_headbanger()

    def _activate_headbanger(self):
        obj = self.new_object()
        obj.x = random.randint(0, Board.BOARD_WIDTH)
        obj.y = random.randint(0, Board.BOARD_HEIGHT)
        obj.type = game_types.HeadBanger
        self.activate_object(obj)
