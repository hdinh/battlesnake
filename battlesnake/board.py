from game_actor import GameActor

Snake_None, Snake_P1, Snake_P2, Snake_P3, Snake_P4 = range(5)
Snake_GoLeft, Snake_GoRight, Snake_GoUp, Snake_GoDown = range(4)


class Board(GameActor):
    BOARD_WIDTH = 55
    BOARD_HEIGHT = 45

    def __init__(self, global_actor):
        GameActor.__init__(self, global_actor)

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
        pass
