from game_object import GameObject


class GameActor:
    def __init__(self, global_actor=None):
        if global_actor != None:
            self.objects = global_actor.objects
        else:
            self.objects = []

    def init(self):
        pass

    def finish(self):
        pass

    def init_game(self):
        self.objects = []

    def finish_game(self):
        pass

    def init_round(self):
        pass

    def finish_round(self):
        pass

    def handle_tick(self):
        pass

    def new_object(self):
        new = GameObject()
        self.objects.append(new)
        return new

    def activate_object(self, obj):
        pass

    def get_object_at(self, x, y):
        for go in self.objects:
            if go.x == x and go.y == y:
                return go
        return None

    def deactivate(self, obj):
        self.objects.remove(obj)
