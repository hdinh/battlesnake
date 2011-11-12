#!/usr/bin/env python
"""
I imagine that this guy will expose a CLI for the game engine.
And / or probably start the web server? I'm lending towards CLI
"""

class Snake:
    def __init__(self):
        pass
    def init(self):
        print('cool')

def main():
    s = SnakeGame()
    s.init()

    s.main_loop()

    s.finish()

if __name__ == '__main__':
    main()
