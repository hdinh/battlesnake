import threading


class Engine(object):
    def __init__(self, game, options):
        self.game = game
        self.options = options

    def run_game(self):
        self.finished = threading.Event()
        self.game.init_game()
        self.begin_timer()
        self.finished.wait()

    def _timer_process(self):
        self.game_handle_tick()

    def begin_timer(self):
        timer = threading.Timer(1.0 / 40, self._timer_process)
        timer.start()

    def game_handle_tick(self):
        self.game.handle_tick()

        if self.game.game_over():
            self.game.finish_game()
            self.finished.set()
        else:
            self.begin_timer()

    def get_moves(self):
        """Wait for each actor to respond"""
        pass
