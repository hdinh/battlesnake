import random
from game_actor import GameActor
from board import Board


class Fruit(GameActor):
    TICK_FREQ = 12
    MAX_FRUITS = 50

    def __init__(self, global_actor):
        GameActor.__init__(self, global_actor)

        self.current_tick = 0
        self.num_fruits = 0

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
        if self.current_tick < Fruit.TICK_FREQ:
            return

        self.current_tick = 0
        if self.num_fruits < Fruit.MAX_FRUITS and random.random() < .1:
            self.num_fruits += 1
            self._activate_fruit()

    def _activate_fruit(self):
        obj = self.new_object()
        obj.x = random.randint(0, Board.BOARD_WIDTH)
        obj.y = random.randint(0, Board.BOARD_HEIGHT)
        self.activate_object(obj)
