import numpy as np

class World:
    def __init__(self, size=(50,50)):
        self.size = size
        self.energy = np.zeros(size)

    def initialize_random(self):
        self.energy = np.random.uniform(20, 80, self.size)

    def step(self):
        # simple diffusion
        self.energy = (self.energy + np.roll(self.energy,1,0) + np.roll(self.energy,-1,0) + np.roll(self.energy,1,1) + np.roll(self.energy,-1,1)) / 5.0

    def get_energy(self, pos):
        x, y = int(pos[0]) % self.size[0], int(pos[1]) % self.size[1]
        return self.energy[x, y]

    def consume_energy(self, pos, amount):
        x, y = int(pos[0]) % self.size[0], int(pos[1]) % self.size[1]
        taken = min(self.energy[x, y], amount)
        self.energy[x, y] -= taken
        return taken
