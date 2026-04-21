"""
Symbolization System V1
Implements:
- Feature extraction from sensors
- Symbol (concept) creation
- Associative links between symbols (mindpathing lite)
Aligned with A7DO Cognitive docs (v2.0)
"""

from collections import defaultdict

class Symbol:
    def __init__(self, name, features):
        self.name = name
        self.features = features  # compressed representation
        self.activations = 0


class SymbolizationSystemV1:
    def __init__(self):
        self.symbols = {}  # name -> Symbol
        self.associations = defaultdict(dict)  # symbol_a -> {symbol_b: weight}

    def extract_features(self, sensor_data, identity_data):
        return {
            "stable": sensor_data.get("balance", {}).get("stable", True),
            "moving": sensor_data.get("motion", {}).get("velocity", 0) > 0.01,
            "identity": identity_data.get("identity", "unknown")
        }

    def get_or_create_symbol(self, features):
        key = str(features)
        if key not in self.symbols:
            name = f"CONCEPT_{len(self.symbols)}"
            self.symbols[key] = Symbol(name, features)
        symbol = self.symbols[key]
        symbol.activations += 1
        return symbol

    def link(self, sym_a, sym_b, weight=1.0):
        if sym_b.name not in self.associations[sym_a.name]:
            self.associations[sym_a.name][sym_b.name] = 0
        self.associations[sym_a.name][sym_b.name] += weight

    def get_associations(self, symbol):
        return self.associations.get(symbol.name, {})

    def process(self, sensor_data, identity_data, previous_symbol=None):
        features = self.extract_features(sensor_data, identity_data)
        current_symbol = self.get_or_create_symbol(features)
        if previous_symbol is not None:
            self.link(previous_symbol, current_symbol)
        return current_symbol

    def get_symbols(self):
        return {k: v.name for k, v in self.symbols.items()}

    def get_graph(self):
        return dict(self.associations)
