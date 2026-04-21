"""
Balance System V1
Implements center of mass (CoM) and basic stability control
"""

class BalanceSystemV1:
    def __init__(self, biomechanics, fk_system):
        self.biomechanics = biomechanics
        self.fk = fk_system

    def compute_com(self):
        """
        Approximate CoM using key segments
        """
        positions = self.fk.compute_all()

        segments = [
            {"mass": 10, "x": positions["spine"]["base"][0], "y": positions["spine"]["base"][1]},
            {"mass": 5, "x": positions["spine"]["head"][0], "y": positions["spine"]["head"][1]},
            {"mass": 8, "x": positions["left_leg"]["knee"][0], "y": positions["left_leg"]["knee"][1]},
            {"mass": 6, "x": positions["left_leg"]["foot"][0], "y": positions["left_leg"]["foot"][1]}
        ]

        return self.biomechanics.center_of_mass(segments)

    def base_of_support(self):
        """
        Define foot contact region (simplified)
        """
        positions = self.fk.compute_all()
        foot_x = positions["left_leg"]["foot"][0]

        return (foot_x - 0.1, foot_x + 0.1)

    def is_stable(self):
        com_x, _ = self.compute_com()
        foot_min, foot_max = self.base_of_support()

        return self.biomechanics.is_balanced(com_x, foot_min, foot_max)

    def get_state(self):
        com = self.compute_com()
        foot = self.base_of_support()

        return {
            "center_of_mass": com,
            "base_of_support": foot,
            "stable": self.is_stable()
        }
