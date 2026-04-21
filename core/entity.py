from body.skeleton import Bone
from body.muscles import Muscle

class Entity:
    def __init__(self):

        # Bones
        self.bones = {
            "scapula": Bone("scapula"),
            "humerus": Bone("humerus"),
            "radius": Bone("radius"),
        }

        # Muscles
        self.muscles = {
            "biceps": Muscle(
                name="biceps",
                origin="scapula",
                insertion="radius",
                strength=0.8
            )
        }

        self.energy = 100
        self.alive = True

    def update(self):
        for muscle in self.muscles.values():
            force = muscle.contract()
            # movement logic comes next step

        if self.energy <= 0:
            self.alive = False
