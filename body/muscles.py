class Muscle:
    def __init__(self, name, origin, insertion, strength=1.0):
        self.name = name
        self.origin = origin
        self.insertion = insertion
        self.strength = strength
        self.activation = 0.0

    def contract(self):
        force = self.strength * self.activation
        return force
