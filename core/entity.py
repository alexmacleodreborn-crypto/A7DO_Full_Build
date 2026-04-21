class Entity:
    def __init__(self):
        self.bones = {}
        self.muscles = {}
        self.energy = 100
        self.alive = True

    def update(self):
        if self.energy <= 0:
            self.alive = False
