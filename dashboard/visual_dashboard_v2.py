"""
A7DO Visual Dashboard V2 (Full System View)
Run with: streamlit run dashboard/visual_dashboard_v2.py
"""

import streamlit as st
import cv2

from human_system.sensors.vision_voice_system_v1 import VisionSystem
from human_system.identity.self_identity_v1 import SelfIdentityV1
from human_system.cognition.symbolization_system_v1 import SymbolizationSystemV1
from human_system.cognition.mindpathing_system_v1 import MindpathingSystemV1
from human_system.control.decision_system_v1 import DecisionSystemV1

st.set_page_config(layout="wide")
st.title("A7DO Dashboard V2 - Full Cognitive View")

# Init systems
vision = VisionSystem()
identity = SelfIdentityV1()
symbol_system = SymbolizationSystemV1()
mind = MindpathingSystemV1(symbol_system)
decision_system = DecisionSystemV1()

prev_symbol = None

# Layout
col1, col2, col3 = st.columns(3)

# Controls
if st.button("Register Self"):
    frame = vision.get_frame()
    if frame is not None:
        identity.register_self(frame)
        st.success("Face registered")

frame_placeholder = col1.empty()
state_placeholder = col2.empty()
thought_placeholder = col3.empty()

# Main loop
while True:
    frame = vision.get_frame()
    if frame is None:
        continue

    identity_data = identity.get_identity_state(frame)

    sensor_data = {
        "balance": {"stable": True},
        "motion": {"velocity": 0}
    }

    symbol = symbol_system.process(sensor_data, identity_data, prev_symbol)

    if mind.current_symbol is None:
        mind.set_start(symbol)

    thought_chain = mind.run_sequence(3)

    decision = decision_system.decide(sensor_data, identity_data)

    # Draw identity on frame
    cv2.putText(frame, identity_data["identity"], (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

    state_placeholder.json({
        "identity": identity_data,
        "symbol": symbol.name,
        "decision": decision
    })

    thought_placeholder.write({
        "thought_chain": thought_chain
    })

    prev_symbol = symbol
