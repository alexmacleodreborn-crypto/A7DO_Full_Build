import numpy as np

class BodyPhysics:
    def __init__(self, position=(0.0, 0.0), mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array([0.0, 0.0], dtype=float)
        self.acceleration = np.array([0.0, 0.0], dtype=float)

        self.mass = mass
        self.friction = 0.90
        self.max_speed = 5.0

    def apply_force(self, force):
        force = np.array(force, dtype=float)
        self.acceleration += force / self.mass

    def update(self):
        self.velocity += self.acceleration

        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed

        self.velocity *= self.friction
        self.position += self.velocity

        self.acceleration[:] = 0.0

    def get_state(self):
        return {
            "position": self.position.copy(),
            "velocity": self.velocity.copy()
        }
