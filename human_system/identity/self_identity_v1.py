class SelfIdentityV1:
    def __init__(self):
        self.registered = False

    def register_self(self, frame):
        self.registered = True
        return True

    def get_identity_state(self, frame):
        return {
            "identity": "self" if self.registered else "unknown",
            "registered": self.registered
        }