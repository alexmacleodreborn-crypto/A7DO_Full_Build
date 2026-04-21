from body.body_physics import BodyPhysics
import numpy as np

class Entity:
    def __init__(self, world, position=(0,0)):
        self.world = world
        self.body = BodyPhysics(position=position, mass=1.0)
        self.energy = 100.0
        self.alive = True

    def update(self):
        if not self.alive:
            return

        force = self.decide()
        self.body.apply_force(force)
        self.body.update()

        # consume world energy
        gained = self.world.consume_energy(self.body.position, 1.0)
        self.energy += gained

        # metabolic cost
        self.energy -= 0.2

        if self.energy <= 0:
            self.alive = False

    def decide(self):
        return np.random.uniform(-1,1,2)

    def get_state(self):
        return {
            "pos": self.body.position,
            "energy": self.energy
        }
