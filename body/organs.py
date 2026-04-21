class Heart:
    def __init__(self):
        self.rate = 70
        self.output = 1.0

    def pump(self):
        return self.output


class Lungs:
    def __init__(self):
        self.oxygen_level = 1.0

    def breathe(self):
        return self.oxygen_level


class Brain:
    def __init__(self):
        self.signal_strength = 1.0

    def think(self):
        return self.signal_strength


class Stomach:
    def __init__(self):
        self.energy_store = 100.0

    def digest(self, amount=1.0):
        gained = min(self.energy_store, amount)
        self.energy_store -= gained
        return gained


class Liver:
    def __init__(self):
        self.balance = 1.0

    def regulate(self, energy):
        return energy * self.balance
