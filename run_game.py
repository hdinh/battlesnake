#!/usr/bin/env python
"""
I imagine that this guy will expose a CLI for the game engine.
And / or probably start the web server? I'm lending towards CLI
"""
import properties
from engine import run_game

class Snake:
    def __init__(self):
        pass
    def init(self):
        print('cool')

def main():
    prop = properties.Properties()
    game_options = {
        "speed": 10
    }
    game = SnakeGame()
    game.init()

    run_game(game)

    game.finish()

if __name__ == '__main__':
    main()
