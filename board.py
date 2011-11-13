from game_object import GameObject

Snake_None, Snake_P1, Snake_P2, Snake_P3, Snake_P4 = range(5)
Snake_GoLeft, Snake_GoRight, Snake_GoUp, Snake_GoDown = range(4)


class Board(GameObject):
    BOARD_WIDTH  = 55
    BOARD_HEIGHT = 45

    def __init__(self):
        self.board = [Snake_None] * (Board.BOARD_WIDTH * Board.BOARD_HEIGHT)

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
