#!/usr/bin/env python
"""
I imagine that this guy will expose a CLI for the game engine.
And / or probably start the web server? I'm lending towards CLI
"""
from engine import Engine
from battlesnake import BattleSnake


def main():
    options = {
        "turntime": 100
    }

    game = BattleSnake()
    game.init()

    engine = Engine(game, options)
    engine.run_game()

    game.finish()

if __name__ == '__main__':
    main()
