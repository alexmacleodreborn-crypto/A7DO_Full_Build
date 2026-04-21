"""
Motion System V1
Applies muscle forces to joints and updates joint angles
"""

class MotionSystem:
    def __init__(self, joint_system, muscle_system):
        self.joint_system = joint_system
        self.muscle_system = muscle_system

        # store joint states
        self.joint_states = {}

        for joint in joint_system.joints:
            self.joint_states[joint["name"]] = {
                "angle": 0.0,
                "velocity": 0.0
            }

    def step(self):
        # get forces from muscles
        joint_forces = self.muscle_system.compute_joint_forces()

        for joint_name, force in joint_forces.items():
            state = self.joint_states.get(joint_name)

            if not state:
                continue

            # simple physics
            state["velocity"] += force * 0.1
            state["angle"] += state["velocity"]

            # damping
            state["velocity"] *= 0.9

            # clamp to joint limits
            joint = self.joint_system.get_joint(joint_name)
            if joint and "range" in joint:
                r = joint["range"]

                # assume x-axis for hinge simplicity
                if "x" in r:
                    min_a, max_a = r["x"]
                    state["angle"] = max(min(state["angle"], max_a), min_a)

    def get_joint_state(self, joint_name):
        return self.joint_states.get(joint_name, None)

    def get_all_states(self):
        return self.joint_states
