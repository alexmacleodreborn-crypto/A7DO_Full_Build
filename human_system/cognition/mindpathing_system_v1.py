"""
Mindpathing System V1
Implements associative traversal over symbol graph
Inspired by A7DO Cognitive Engine (DMN + Executive Routing)
"""

import random

class MindpathingSystemV1:
    def __init__(self, symbol_system):
        self.symbol_system = symbol_system
        self.current_symbol = None

    def set_start(self, symbol):
        self.current_symbol = symbol

    def step(self, mode="default"):
        """
        Traverse symbol graph
        mode:
        - default: random associative walk (DMN)
        - focused: strongest association (goal-directed)
        """
        if self.current_symbol is None:
            return None

        associations = self.symbol_system.get_associations(self.current_symbol)

        if not associations:
            return self.current_symbol

        if mode == "default":
            # random exploration
            next_symbol_name = random.choice(list(associations.keys()))
        else:
            # strongest learned path
            next_symbol_name = max(associations, key=associations.get)

        # find symbol object
        for sym in self.symbol_system.symbols.values():
            if sym.name == next_symbol_name:
                self.current_symbol = sym
                break

        return self.current_symbol

    def run_sequence(self, steps=5, mode="default"):
        """
        Generate a chain of thoughts
        """
        sequence = []

        for _ in range(steps):
            sym = self.step(mode=mode)
            if sym is None:
                break
            sequence.append(sym.name)

        return sequence

    def get_current(self):
        return self.current_symbol.name if self.current_symbol else None
