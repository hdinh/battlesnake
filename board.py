from game_object import GameObject

class Board(GameObject):
    BOARDWIDTH  = 92
    BOARDHEIGHT = 92

    def __init__(self):
        self.board = [None] * (Board.BOARDWIDTH * Board.BOARDHEIGHT)

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
