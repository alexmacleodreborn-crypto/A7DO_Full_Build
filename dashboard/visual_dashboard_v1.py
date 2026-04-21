"""
A7DO Visual Dashboard V1
Run with: streamlit run dashboard/visual_dashboard_v1.py
"""

import streamlit as st
import cv2

from human_system.sensors.vision_voice_system_v1 import VisionSystem
from human_system.identity.self_identity_v1 import SelfIdentityV1

st.set_page_config(layout="wide")

st.title("A7DO Live Dashboard")

vision = VisionSystem()
identity = SelfIdentityV1()

col1, col2 = st.columns(2)

# Register button
if st.button("Register Self"):
    frame = vision.get_frame()
    if frame is not None:
        identity.register_self(frame)
        st.success("Face registered as self")

# Live loop
frame_placeholder = col1.empty()
info_placeholder = col2.empty()

while True:
    frame = vision.get_frame()
    if frame is None:
        continue

    state = identity.get_identity_state(frame)

    cv2.putText(frame, state["identity"], (30, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

    info_placeholder.json({
        "identity": state["identity"],
        "registered": state["registered"]
    })
