"""
Biomechanics System V1
Implements torque, lever mechanics, and basic balance
Based on A7DO Physics Layer
"""

import math

class Biomechanics:
    def __init__(self):
        pass

    def torque(self, force, moment_arm, angle_deg):
        """
        τ = F * r * sin(θ)
        """
        theta = math.radians(angle_deg)
        return force * moment_arm * math.sin(theta)

    def mechanical_advantage(self, effort_dist, load_dist):
        """
        MA = d_effort / d_load
        """
        if load_dist == 0:
            return 0
        return effort_dist / load_dist

    def moment_of_inertia(self, mass, radius):
        """
        I = m * k^2
        """
        return mass * (radius ** 2)

    def center_of_mass(self, segments):
        """
        segments: list of {mass, x, y}
        """
        total_mass = sum(s["mass"] for s in segments)
        if total_mass == 0:
            return (0, 0)

        x = sum(s["mass"] * s["x"] for s in segments) / total_mass
        y = sum(s["mass"] * s["y"] for s in segments) / total_mass

        return (x, y)

    def is_balanced(self, com_x, foot_min_x, foot_max_x):
        """
        Check if center of mass is within base of support
        """
        return foot_min_x <= com_x <= foot_max_x
