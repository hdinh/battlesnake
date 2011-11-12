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

    def init()
        pass

    def finish()
        pass

    def handle_tick(self):
        pass

def run(game):
    pass
