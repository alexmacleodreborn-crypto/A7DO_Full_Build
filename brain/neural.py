import random

class NeuralSystem:
    """
    Simple brain v1:
    - senses internal state (energy)
    - produces signals for muscles
    - basic feedback loop
    """

    def __init__(self):
        self.state = "idle"  # idle, explore, conserve
        self.signal_map = {}

    def sense(self, entity):
        energy = entity.energy

        if energy < 20:
            self.state = "conserve"
        elif energy < 60:
            self.state = "idle"
        else:
            self.state = "explore"

    def decide(self, entity):
        signals = {}

        for name in entity.muscles.keys():
            if self.state == "conserve":
                signals[name] = 0.1
            elif self.state == "idle":
                signals[name] = 0.3
            elif self.state == "explore":
                signals[name] = random.uniform(0.4, 1.0)

        self.signal_map = signals
        return signals

    def act(self, entity):
        for name, muscle in entity.muscles.items():
            activation = self.signal_map.get(name, 0.0)
            muscle.activation = activation

    def step(self, entity):
        self.sense(entity)
        self.decide(entity)
        self.act(entity)
