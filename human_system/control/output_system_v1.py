"""
Output System V1
Converts decisions into actions (movement + speech)
"""

class OutputSystemV1:
    def __init__(self, neural_system, voice_system):
        self.neural = neural_system
        self.voice = voice_system

    def act(self, decision):
        """
        decision: dict with optional keys
        - movement: {joint: angle}
        - speech: string
        """

        # movement output
        if "movement" in decision:
            for joint, angle in decision["movement"].items():
                self.neural.set_target(joint, angle)

        # speech output
        if "speech" in decision:
            self.voice.speak(decision["speech"])

    def idle(self):
        """
        Default behaviour when no decision
        """
        pass
