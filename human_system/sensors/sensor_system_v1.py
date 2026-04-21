"""
Sensor System V1
Provides basic perception: balance, joint position, and ground contact
"""

class SensorSystemV1:
    def __init__(self, motion_system, balance_system, forward_motion):
        self.motion = motion_system
        self.balance = balance_system
        self.forward_motion = forward_motion

    def get_joint_positions(self):
        """
        Proprioception: joint angles
        """
        return self.motion.get_all_states()

    def get_balance(self):
        """
        Vestibular-like sense (balance)
        """
        return self.balance.get_state()

    def get_ground_contact(self):
        """
        Foot contact sensing
        """
        return {
            "left_foot_contact": self.forward_motion.detect_foot_contact()
        }

    def get_body_state(self):
        """
        Combined sensor output
        """
        return {
            "joints": self.get_joint_positions(),
            "balance": self.get_balance(),
            "ground": self.get_ground_contact(),
            "motion": self.forward_motion.get_state()
        }
