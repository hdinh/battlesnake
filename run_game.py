#!/usr/bin/env python
"""
I imagine that this guy will expose a CLI for the game engine.
And / or probably start the web server? I'm lending towards CLI
"""
from engine import run_game
from snake import Snake

def main():
    game = Snake()
    game.init()

    run_game(game)

    game.finish()

if __name__ == '__main__':
    main()
