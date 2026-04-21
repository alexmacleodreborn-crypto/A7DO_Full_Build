"""
Decision System V1
Connects sensors + identity to output actions
"""

class DecisionSystemV1:
    def __init__(self):
        pass

    def decide(self, sensor_data, identity_data):
        """
        Basic rule-based decision making
        """

        decision = {}

        # Identity-based behaviour
        if identity_data.get("identity") == "self":
            decision["speech"] = "I can see myself"
            decision["movement"] = {
                "hip_L": 5,
                "knee_L": 10
            }

        elif identity_data.get("identity") == "other":
            decision["speech"] = "I see someone else"

        # Balance correction priority
        balance = sensor_data.get("balance", {})
        if not balance.get("stable", True):
            decision["movement"] = {
                "hip_L": 10,
                "knee_L": 20
            }
            decision["speech"] = "Stabilising"

        # Default fallback
        if not decision:
            decision["speech"] = "Idle"

        return decision
