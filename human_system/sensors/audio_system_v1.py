import threading
import time

class AudioSystemV1:
    def __init__(self):
        self.listening = False
        self.last_heard = None

    def start(self):
        self.listening = True
        thread = threading.Thread(target=self._listen_loop, daemon=True)
        thread.start()

    def _listen_loop(self):
        while self.listening:
            self.last_heard = "ambient_noise"
            time.sleep(2)

    def get_state(self):
        return {
            "hearing": self.last_heard
        }
