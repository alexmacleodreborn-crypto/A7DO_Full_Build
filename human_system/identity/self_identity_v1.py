"""
Self Identity System V1
Links camera input to a persistent identity ("self") using face recognition
"""

import cv2
import face_recognition

class SelfIdentityV1:
    def __init__(self):
        self.known_face_encoding = None
        self.identity_label = "unknown"

    def register_self(self, frame):
        """
        Capture and store the user's face as 'self'
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)

        if encodings:
            self.known_face_encoding = encodings[0]
            self.identity_label = "self"
            return True
        return False

    def identify(self, frame):
        """
        Compare current frame to stored identity
        """
        if self.known_face_encoding is None:
            return "unregistered"

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)

        for encoding in encodings:
            match = face_recognition.compare_faces([self.known_face_encoding], encoding)[0]
            if match:
                return "self"

        return "other"

    def get_identity_state(self, frame):
        """
        Full identity perception output
        """
        return {
            "identity": self.identify(frame),
            "registered": self.known_face_encoding is not None
        }
