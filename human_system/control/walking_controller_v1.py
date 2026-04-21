"""
Walking Controller V1
Implements a simple gait cycle using balance + neural control
"""

import math

class WalkingControllerV1:
    def __init__(self, neural_system, motion_system):
        self.neural = neural_system
        self.motion = motion_system
        self.time = 0.0

    def step(self, dt=0.1):
        """
        Basic gait cycle using sinusoidal motion
        """
        self.time += dt

        # oscillating targets
        hip_angle = 20 * math.sin(self.time)
        knee_angle = 30 * (math.sin(self.time) + 1) / 2  # always positive

        # send targets to neural system
        self.neural.set_target("hip_L", hip_angle)
        self.neural.set_target("knee_L", knee_angle)

    def get_state(self):
        return {
            "time": self.time
        }
