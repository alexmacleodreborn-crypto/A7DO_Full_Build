"""
Neural System V2 (Closed Feedback Loop)
Adds proprioception + PID-based correction
"""

class NeuralSystemV2:
    def __init__(self, muscle_system, motion_system, pid_controller):
        self.muscle_system = muscle_system
        self.motion_system = motion_system
        self.pid = pid_controller

        # target joint angles
        self.targets = {}

    def set_target(self, joint_name, angle):
        self.targets[joint_name] = angle

    def step(self):
        """
        Closed-loop control:
        target → compare → correct → activate muscles
        """

        for joint_name, target_angle in self.targets.items():
            state = self.motion_system.get_joint_state(joint_name)

            if not state:
                continue

            current_angle = state["angle"]

            # PID correction
            correction = self.pid.compute(target_angle, current_angle)

            # map correction to muscles (simplified)
            if correction > 0:
                # extensor
                self.muscle_system.activate(f"{joint_name}_extensor", min(abs(correction), 1.0))
                self.muscle_system.activate(f"{joint_name}_flexor", 0)
            else:
                # flexor
                self.muscle_system.activate(f"{joint_name}_flexor", min(abs(correction), 1.0))
                self.muscle_system.activate(f"{joint_name}_extensor", 0)

    def get_targets(self):
        return self.targets
