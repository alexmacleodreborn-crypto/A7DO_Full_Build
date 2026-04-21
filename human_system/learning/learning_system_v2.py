"""
Learning System V2
Implements structured learning inspired by A7DO Cognitive Engine:
- Short-term memory (buffer)
- Long-term memory (consolidated)
- Reward-weighted learning
- Simple feature compression (symbolization)
"""

class LearningSystemV2:
    def __init__(self):
        self.short_term = []   # RAM-like buffer
        self.long_term = {}    # consolidated memory
        self.policy = {}

    def compress_state(self, state):
        """
        Reduce raw sensor state into simple symbolic representation
        """
        balance = state.get("balance", {}).get("stable", True)
        motion = state.get("motion", {}).get("velocity", 0)

        return {
            "stable": balance,
            "moving": motion > 0.01
        }

    def record(self, state, action, reward):
        """
        Store in short-term memory
        """
        compressed = self.compress_state(state)
        self.short_term.append({
            "state": compressed,
            "action": action,
            "reward": reward
        })

    def consolidate(self):
        """
        Move important experiences into long-term memory
        """
        for entry in self.short_term:
            if entry["reward"] > 0:
                key = str(entry["state"])
                if key not in self.long_term:
                    self.long_term[key] = []
                self.long_term[key].append(entry)

        # clear short-term (simulate sleep flush)
        self.short_term = []

    def update_policy(self):
        """
        Build policy from long-term memory
        """
        for state, experiences in self.long_term.items():
            if state not in self.policy:
                self.policy[state] = {}

            for entry in experiences:
                action_key = str(entry["action"])
                if action_key not in self.policy[state]:
                    self.policy[state][action_key] = 0

                self.policy[state][action_key] += entry["reward"]

    def choose_action(self, state, default_action):
        """
        Select best known action or fallback
        """
        compressed = str(self.compress_state(state))

        if compressed in self.policy and self.policy[compressed]:
            return max(self.policy[compressed], key=self.policy[compressed].get)

        return default_action

    def get_memory(self):
        return {
            "short_term": self.short_term,
            "long_term": self.long_term
        }

    def get_policy(self):
        return self.policy
