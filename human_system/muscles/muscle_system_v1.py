"""
Muscle System V1
Defines muscles, their attachments, and how they generate movement via joints
"""

MUSCLE_TYPES = {
    "flexor": "decreases joint angle",
    "extensor": "increases joint angle",
    "stabilizer": "maintains position"
}

MUSCLES = [
    {
        "name": "quadriceps_L",
        "type": "extensor",
        "origin": "pelvis",
        "insertion": "tibia_L",
        "joint": "knee_L",
        "strength": 1.0
    },
    {
        "name": "hamstring_L",
        "type": "flexor",
        "origin": "pelvis",
        "insertion": "tibia_L",
        "joint": "knee_L",
        "strength": 0.9
    },
    {
        "name": "glute_L",
        "type": "extensor",
        "origin": "pelvis",
        "insertion": "femur_L",
        "joint": "hip_L",
        "strength": 1.2
    },
    {
        "name": "neck_stabilizer",
        "type": "stabilizer",
        "origin": "spine",
        "insertion": "skull",
        "joint": "neck",
        "strength": 0.5
    }
]

class MuscleSystem:
    def __init__(self, muscles):
        self.muscles = muscles

    def activate(self, muscle_name, level):
        for m in self.muscles:
            if m["name"] == muscle_name:
                m["activation"] = level

    def compute_joint_forces(self):
        joint_forces = {}

        for m in self.muscles:
            activation = m.get("activation", 0)
            force = activation * m["strength"]

            joint = m["joint"]

            if joint not in joint_forces:
                joint_forces[joint] = 0

            if m["type"] == "flexor":
                joint_forces[joint] -= force
            elif m["type"] == "extensor":
                joint_forces[joint] += force

        return joint_forces
