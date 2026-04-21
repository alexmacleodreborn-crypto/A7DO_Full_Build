"""
Learning System V1
Adds simple reinforcement learning via reward feedback
"""

class LearningSystemV1:
    def __init__(self):
        self.memory = []
        self.policy = {}

    def record(self, state, action, reward):
        """
        Store experience
        """
        self.memory.append({
            "state": state,
            "action": action,
            "reward": reward
        })

    def update_policy(self):
        """
        Very simple learning: reinforce actions with positive reward
        """
        for entry in self.memory:
            key = str(entry["state"])
            if key not in self.policy:
                self.policy[key] = {}

            action_key = str(entry["action"])
            if action_key not in self.policy[key]:
                self.policy[key][action_key] = 0

            self.policy[key][action_key] += entry["reward"]

    def choose_action(self, state, default_action):
        """
        Choose best known action or fallback
        """
        key = str(state)

        if key in self.policy and self.policy[key]:
            return max(self.policy[key], key=self.policy[key].get)

        return default_action

    def get_memory(self):
        return self.memory

    def get_policy(self):
        return self.policy
