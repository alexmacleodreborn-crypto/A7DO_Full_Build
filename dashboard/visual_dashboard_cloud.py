import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from human_system.sensors.vision_system_safe import VisionSystemSafe
from human_system.identity.self_identity_v1 import SelfIdentityV1
from human_system.cognition.symbolization_system_v1 import SymbolizationSystemV1
from human_system.cognition.mindpathing_system_v1 import MindpathingSystemV1
from human_system.control.decision_system_v1 import DecisionSystemV1

st.set_page_config(layout="wide")
st.title("A7DO Cloud Dashboard (Safe Mode)")

# Init systems
if "vision" not in st.session_state:
    st.session_state.vision = VisionSystemSafe()
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

if st.button("Register Self (Simulated)"):
    st.success("Simulated identity registered")

frame = vision.get_frame()

identity_data = {"identity": "self", "registered": True}

sensor_data = {
    "balance": {"stable": True},
    "motion": {"velocity": 0}
}

symbol = symbol_system.process(sensor_data, identity_data, st.session_state.prev_symbol)

if mind.current_symbol is None:
    mind.set_start(symbol)

thought = mind.run_sequence(3)

decision = decision_system.decide(sensor_data, identity_data)

col1.image(frame)

col2.json({
    "identity": identity_data,
    "symbol": symbol.name,
    "decision": decision
})

col3.write({
    "thought_chain": thought
})

st.session_state.prev_symbol = symbol
