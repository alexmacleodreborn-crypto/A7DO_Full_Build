"""
Forward Kinematics V1
Computes bone positions from joint angles
"""

import math

class ForwardKinematics:
    def __init__(self, joint_system, motion_system):
        self.joint_system = joint_system
        self.motion_system = motion_system

        # simple bone lengths (placeholder, will later come from bone system)
        self.bone_lengths = {
            "femur_L": 0.5,
            "tibia_L": 0.5,
            "spine": 0.7,
            "skull": 0.2
        }

    def compute_leg_L(self, origin=(0,0)):
        """
        Compute left leg positions (2D)
        """

        hip_angle = self.motion_system.get_joint_state("hip_L")["angle"]
        knee_angle = self.motion_system.get_joint_state("knee_L")["angle"]

        x, y = origin

        # femur
        femur_len = self.bone_lengths["femur_L"]
        knee_x = x + femur_len * math.cos(math.radians(hip_angle))
        knee_y = y + femur_len * math.sin(math.radians(hip_angle))

        # tibia
        tibia_len = self.bone_lengths["tibia_L"]
        total_angle = hip_angle + knee_angle
        foot_x = knee_x + tibia_len * math.cos(math.radians(total_angle))
        foot_y = knee_y + tibia_len * math.sin(math.radians(total_angle))

        return {
            "hip": (x, y),
            "knee": (knee_x, knee_y),
            "foot": (foot_x, foot_y)
        }

    def compute_spine(self, origin=(0,0)):
        neck_angle = self.motion_system.get_joint_state("neck")["angle"]

        x, y = origin
        spine_len = self.bone_lengths["spine"]

        head_x = x + spine_len * math.cos(math.radians(neck_angle))
        head_y = y + spine_len * math.sin(math.radians(neck_angle))

        return {
            "base": (x, y),
            "head": (head_x, head_y)
        }

    def compute_all(self):
        return {
            "left_leg": self.compute_leg_L(origin=(0,0)),
            "spine": self.compute_spine(origin=(0,0))
        }
