"""
Walking Controller V2 (Two-Leg Gait + Weight Shift)
Introduces left/right leg coordination and center-of-mass shifting
"""

import math

class WalkingControllerV2:
    def __init__(self, neural_system, balance_controller):
        self.neural = neural_system
        self.balance_controller = balance_controller
        self.time = 0.0
        self.phase = 0  # 0 = left stance, 1 = right stance

    def step(self, dt=0.1):
        self.time += dt

        # alternate phase every cycle
        if int(self.time) % 2 == 0:
            self.phase = 0
        else:
            self.phase = 1

        swing = math.sin(self.time)

        if self.phase == 0:
            # LEFT LEG = stance (support)
            self.neural.set_target("hip_L", 5)
            self.neural.set_target("knee_L", 15)

            # RIGHT LEG = swing (forward motion)
            self.neural.set_target("hip_R", 20 * swing)
            self.neural.set_target("knee_R", 30 * (swing + 1) / 2)

            # shift balance to left
            self.neural.set_target("hip_L", 10)

        else:
            # RIGHT LEG = stance
            self.neural.set_target("hip_R", 5)
            self.neural.set_target("knee_R", 15)

            # LEFT LEG = swing
            self.neural.set_target("hip_L", 20 * swing)
            self.neural.set_target("knee_L", 30 * (swing + 1) / 2)

            # shift balance to right
            self.neural.set_target("hip_R", 10)

        # always run balance correction
        self.balance_controller.step()

    def get_state(self):
        return {
            "time": self.time,
            "phase": "left_stance" if self.phase == 0 else "right_stance"
        }
