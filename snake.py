from game import Game
from score import Score
from board import Board
from worm import Worm
from mushroom import Mushroom
from scull import Scull
from headbanger import HeadBanger
from pill import Pill
from fruit import Fruit
from game_actor import GameActor

from qtboard import QtBoard


class Snake(Game):
    def __init__(self, game_options=None):
        global_actor = GameActor()

        self.actors = []
        self.actors.append(Score(global_actor))
        #self.actors.append(Board())
        self.actors.append(QtBoard(global_actor))
        self.actors.append(Worm(global_actor))
        self.actors.append(Mushroom(global_actor))
        self.actors.append(Scull(global_actor))
        self.actors.append(HeadBanger(global_actor))
        self.actors.append(Pill(global_actor))
        self.actors.append(Fruit(global_actor))

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
