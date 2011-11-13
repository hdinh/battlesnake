class Game:
    def __init__(self):
        pass

    def game_over(self):
        pass

    def init_game(self):
        pass

    def finish_game(self):
        pass

    def handle_tick(self):
        pass

    # Experimental
    def do_moves(self, player, move):
        orders = []
        self.validate_order(player, move)

    def validate_order(self, player, move):
        pass

    def do_orders(self, player, move):
        pass
