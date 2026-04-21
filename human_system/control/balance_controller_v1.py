"""
Balance Controller V1
Connects balance system to neural control to maintain stability
"""

class BalanceControllerV1:
    def __init__(self, balance_system, neural_system):
        self.balance = balance_system
        self.neural = neural_system

    def step(self):
        state = self.balance.get_state()

        com_x, _ = state["center_of_mass"]
        foot_min, foot_max = state["base_of_support"]

        # If COM is drifting left/right, adjust hip
        center = (foot_min + foot_max) / 2
        error = center - com_x

        # simple correction strategy
        if abs(error) > 0.01:
            correction_angle = error * 50  # gain factor

            # adjust hip to bring COM back
            self.neural.set_target("hip_L", correction_angle)

        # keep knee slightly bent for stability
        self.neural.set_target("knee_L", 20)

    def get_status(self):
        return self.balance.get_state()
