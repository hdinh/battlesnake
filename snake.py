from game import Game
from score import Score
from board import Board
from worm import Worm
from mushroom import Mushroom
from scull import Scull
from headbanger import HeadBanger
from pill import Pill
from fruit import Fruit

from qtboard import QtBoard

class Snake(Game):
    def __init__(self, game_options=None):
        self.actors = []
        self.actors.append(Score())
        #self.actors.append(Board())
        self.actors.append(QtBoard())
        self.actors.append(Worm())
        self.actors.append(Mushroom())
        self.actors.append(Scull())
        self.actors.append(HeadBanger())
        self.actors.append(Pill())
        self.actors.append(Fruit())

    def init(self):
        for actor in self.actors:
            actor.init()

    def finish(self):
        for actor in self.actors:
            actor.finish()

    def init_game(self):
        for actor in self.actors:
            actor.init_game()

    def finish_game(self):
        for actor in self.actors:
            actor.finish_game()

    def handle_tick(self):
        for actor in self.actors:
            actor.handle_tick()
