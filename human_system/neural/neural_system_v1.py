"""
Neural System V1
Implements neural activation, latency, and basic motor control
"""

import math
import time

class NeuralSystem:
    def __init__(self):
        self.signals = {}
        self.latency_ms = 120  # average system delay

    def send_signal(self, muscle_name, activation_level):
        """
        Store signal with simulated latency
        """
        self.signals[muscle_name] = {
            "activation": activation_level,
            "timestamp": time.time()
        }

    def process(self, muscle_system):
        current_time = time.time()

        for muscle, data in self.signals.items():
            elapsed = (current_time - data["timestamp"]) * 1000

            if elapsed >= self.latency_ms:
                muscle_system.activate(muscle, data["activation"])


class PIDController:
    def __init__(self, kp=0.5, ki=0.01, kd=0.1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.prev_error = 0

    def compute(self, target, current):
        error = target - current
        self.integral += error
        derivative = error - self.prev_error

        self.prev_error = error

        return (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )
