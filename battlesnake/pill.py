import random
from game_actor import GameActor
from board import Board
import game_types


class Pill(GameActor):
    TICK_FREQ = 30
    MAX_PILLS = 10

    def __init__(self, global_actor):
        GameActor.__init__(self, global_actor)

        self.current_tick = 0
        self.num_pills = 0

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
        if self.current_tick < Pill.TICK_FREQ:
            return

        self.current_tick = 0
        if self.num_pills < Pill.MAX_PILLS and random.random() < .1:
            self.num_pills += 1
            self._activate_pill()

    def _activate_pill(self):
        obj = self.new_object()
        obj.x = random.randint(0, Board.BOARD_WIDTH)
        obj.y = random.randint(0, Board.BOARD_HEIGHT)
        obj.type = game_types.Pill
        self.activate_object(obj)
