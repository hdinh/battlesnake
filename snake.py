from game import Game
from score import Score
from board import Board
from worm import Worm
from mushroom import Mushroom
from scull import Scull
from headbanger import HeadBanger
from pill import Pill
from fruit import Fruit


class Snake(Game):
    def __init__(self, game_options=None):
        self.agents = []
        self.agents.append(Score())
        self.agents.append(Board())
        self.agents.append(Worm())
        self.agents.append(Mushroom())
        self.agents.append(Scull())
        self.agents.append(HeadBanger())
        self.agents.append(Pill())
        self.agents.append(Fruit())

    def init(self):
        for agent in self.agents:
            agent.init()

    def finish(self):
        for agent in self.agents:
            agent.finish()

    def init_game(self):
        for agent in self.agents:
            agent.init_game()

    def finish_game(self):
        for agent in self.agents:
            agent.finish_game()

    def handle_tick(self):
        for agent in self.agents:
            agent.handle_tick()
