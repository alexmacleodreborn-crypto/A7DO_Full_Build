"""
Joint System V1
Defines how bones connect and move
"""

JOINT_TYPES = {
    "ball": {
        "degrees_of_freedom": 3,
        "description": "Full rotation"
    },
    "hinge": {
        "degrees_of_freedom": 1,
        "description": "Forward/back movement"
    },
    "pivot": {
        "degrees_of_freedom": 1,
        "description": "Rotational axis"
    }
}

JOINTS = [
    {
        "name": "hip_L",
        "type": "ball",
        "connects": ["pelvis", "femur_L"],
        "range": {"x": (-120, 120), "y": (-45, 45), "z": (-60, 60)}
    },
    {
        "name": "knee_L",
        "type": "hinge",
        "connects": ["femur_L", "tibia_L"],
        "range": {"x": (0, 140)}
    },
    {
        "name": "neck",
        "type": "pivot",
        "connects": ["spine", "skull"],
        "range": {"y": (-80, 80)}
    }
]

class JointSystem:
    def __init__(self, joints):
        self.joints = joints

    def get_joint(self, name):
        for joint in self.joints:
            if joint["name"] == name:
                return joint
        return None

    def get_connections(self, bone_name):
        connections = []
        for joint in self.joints:
            if bone_name in joint["connects"]:
                connections.append(joint)
        return connections
