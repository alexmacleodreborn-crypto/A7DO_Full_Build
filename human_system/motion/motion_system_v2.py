"""
Motion System V2 (Dynamics Upgrade)
Uses torque, inertia, and damping for realistic motion
"""

class MotionSystemV2:
    def __init__(self, joint_system, muscle_system, biomechanics):
        self.joint_system = joint_system
        self.muscle_system = muscle_system
        self.biomechanics = biomechanics

        self.joint_states = {}

        for joint in joint_system.joints:
            self.joint_states[joint["name"]] = {
                "angle": 0.0,
                "velocity": 0.0,
                "acceleration": 0.0
            }

        # simple defaults (will later come from bone data)
        self.moment_arms = {
            "knee_L": 0.04,
            "hip_L": 0.05,
            "neck": 0.03
        }

        self.inertia = {
            "knee_L": 1.0,
            "hip_L": 2.0,
            "neck": 0.5
        }

    def step(self):
        joint_forces = self.muscle_system.compute_joint_forces()

        for joint_name, force in joint_forces.items():
            state = self.joint_states.get(joint_name)
            if not state:
                continue

            moment_arm = self.moment_arms.get(joint_name, 0.04)
            torque = self.biomechanics.torque(force, moment_arm, 90)

            inertia = self.inertia.get(joint_name, 1.0)

            # τ = I * α  → α = τ / I
            acceleration = torque / inertia

            state["acceleration"] = acceleration
            state["velocity"] += acceleration
            state["angle"] += state["velocity"]

            # damping (friction)
            state["velocity"] *= 0.92

            # clamp to joint limits
            joint = self.joint_system.get_joint(joint_name)
            if joint and "range" in joint:
                r = joint["range"]
                if "x" in r:
                    min_a, max_a = r["x"]
                    state["angle"] = max(min(state["angle"], max_a), min_a)

    def get_joint_state(self, joint_name):
        return self.joint_states.get(joint_name)

    def get_all_states(self):
        return self.joint_states
