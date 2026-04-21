from core.entity_core import Entity
import numpy as np

class Population:
    def __init__(self, world, n=20):
        self.world = world
        self.entities = []

        for _ in range(n):
            pos = (np.random.randint(0,world.size[0]), np.random.randint(0,world.size[1]))
            self.entities.append(Entity(world, pos))

    def step(self):
        alive = []
        for e in self.entities:
            e.update()
            if e.alive:
                alive.append(e)
        self.entities = alive

    def count(self):
        return len(self.entities)
