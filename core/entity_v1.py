from body.skeleton import Bone
from body.muscles import Muscle
from body.organs import Heart, Lungs, Brain, Stomach, Liver

class Entity:
    def __init__(self):
        self.bones = {
            "scapula": Bone("scapula"),
            "humerus": Bone("humerus"),
            "radius": Bone("radius"),
            "pelvis": Bone("pelvis"),
            "femur": Bone("femur"),
            "tibia": Bone("tibia"),
        }

        self.muscles = {
            "biceps": Muscle("biceps", origin="scapula", insertion="radius", strength=0.8),
            "triceps": Muscle("triceps", origin="scapula", insertion="ulna", strength=0.8),
            "quadriceps": Muscle("quadriceps", origin="pelvis", insertion="tibia", strength=1.0),
        }

        self.organs = {
            "heart": Heart(),
            "lungs": Lungs(),
            "brain": Brain(),
            "stomach": Stomach(),
            "liver": Liver()
        }

        self.energy = 100.0
        self.alive = True

    def update(self):
        if not self.alive:
            return

        oxygen = self.organs["lungs"].oxygen_level
        energy_gain = oxygen * 0.5
        self.energy += energy_gain

        total_usage = 0.0
        for m in self.muscles.values():
            force = m.strength * m.activation
            total_usage += force * 0.1

        self.energy -= total_usage

        self.energy *= self.organs["heart"].output
        self.energy *= self.organs["liver"].balance

        if self.energy <= 0:
            self.alive = False

    def get_state(self):
        return {
            "energy": self.energy,
            "alive": self.alive
        }
