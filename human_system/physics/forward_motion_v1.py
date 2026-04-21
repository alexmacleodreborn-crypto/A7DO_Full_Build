"""
Forward Motion System V1
Adds ground interaction and forward translation based on gait
"""

class ForwardMotionV1:
    def __init__(self, fk_system):
        self.fk = fk_system
        self.position = 0.0  # global forward position
        self.velocity = 0.0

    def detect_foot_contact(self):
        """
        Simple contact: foot near ground (y ≈ 0)
        """
        positions = self.fk.compute_all()
        foot_y = positions["left_leg"]["foot"][1]

        return abs(foot_y) < 0.05

    def step(self, gait_speed=0.05):
        """
        If foot is in contact, push body forward
        """
        if self.detect_foot_contact():
            self.velocity += gait_speed

        # apply damping
        self.velocity *= 0.9

        # update position
        self.position += self.velocity

    def get_state(self):
        return {
            "position": self.position,
            "velocity": self.velocity
        }
