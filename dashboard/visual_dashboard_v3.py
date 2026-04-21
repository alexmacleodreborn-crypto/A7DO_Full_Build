import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2

from human_system.sensors.vision_voice_system_v1 import VisionSystem
from human_system.identity.self_identity_v1 import SelfIdentityV1
from human_system.cognition.symbolization_system_v1 import SymbolizationSystemV1
from human_system.cognition.mindpathing_system_v1 import MindpathingSystemV1
from human_system.control.decision_system_v1 import DecisionSystemV1

st.set_page_config(layout="wide")
st.title("A7DO Dashboard V3")

# Persist systems across reruns
if "vision" not in st.session_state:
    st.session_state.vision = VisionSystem()
    st.session_state.identity = SelfIdentityV1()
    st.session_state.symbol_system = SymbolizationSystemV1()
    st.session_state.mind = MindpathingSystemV1(st.session_state.symbol_system)
    st.session_state.decision = DecisionSystemV1()
    st.session_state.prev_symbol = None

vision = st.session_state.vision
identity = st.session_state.identity
symbol_system = st.session_state.symbol_system
mind = st.session_state.mind
decision_system = st.session_state.decision

col1, col2, col3 = st.columns(3)

if st.button("Register Self"):
    frame = vision.get_frame()
    if frame is not None:
        identity.register_self(frame)
        st.success("Registered")

frame = vision.get_frame()

if frame is not None:

    identity_data = identity.get_identity_state(frame)

    # Temporary sensor data
    sensor_data = {
        "balance": {"stable": True},
        "motion": {"velocity": 0}
    }

    symbol = symbol_system.process(sensor_data, identity_data, st.session_state.prev_symbol)

    if mind.current_symbol is None:
        mind.set_start(symbol)

    thought = mind.run_sequence(3)

    decision = decision_system.decide(sensor_data, identity_data)

    # Overlay identity
    cv2.putText(frame, identity_data["identity"], (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    col1.image(frame, channels="RGB")

    col2.json({
        "identity": identity_data,
        "symbol": symbol.name,
        "decision": decision
    })

    col3.write({
        "thought_chain": thought
    })

    st.session_state.prev_symbol = symbol
