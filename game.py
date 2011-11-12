"""
I imagine this guy will the business logic for the game.
"""

from score import Score
from board import Board
from worm import Worm
from mushroom import Mushroom
from scull import Scull
from headbanger import HeadBanger
from pill import Pill
from fruit import Fruit

class SnakeGame:
    def __init__(self, game_options):
        self.agents = []
        self.agents.score(Score())
        self.agents.push(Board())
        self.agents.push(Worm())
        self.agents.push(Mushroom())
        self.agents.push(Scull())
        self.agents.push(HeadBanger())
        self.agents.push(Pill())
        self.agents.push(Fruit())

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

def run(game):
    pass
