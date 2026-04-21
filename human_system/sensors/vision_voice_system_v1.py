"""
Cloud-safe Vision System (no OpenCV)
Uses PIL instead of cv2 for compatibility with Streamlit Cloud
"""

from PIL import Image
import numpy as np

class VisionSystemSafe:
    def __init__(self):
        self.last_frame = None

    def get_frame(self):
        """
        Returns a placeholder frame (since webcam access is limited in cloud)
        """
        img = Image.new('RGB', (320, 240), color=(73, 109, 137))
        self.last_frame = np.array(img)
        return self.last_frame

    def release(self):
        pass
