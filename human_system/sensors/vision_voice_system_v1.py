"""
Vision + Voice System V1
Allows A7DO to use camera (face) and microphone (voice input/output)
"""

import cv2
import speech_recognition as sr
import pyttsx3

class VisionSystem:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()


class VoiceSystem:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except Exception:
                return None

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class VisionVoiceSystem:
    def __init__(self):
        self.vision = VisionSystem()
        self.voice = VoiceSystem()

    def perceive(self):
        return {
            "frame": self.vision.get_frame(),
            "speech": self.voice.listen()
        }

    def respond(self, text):
        self.voice.speak(text)
