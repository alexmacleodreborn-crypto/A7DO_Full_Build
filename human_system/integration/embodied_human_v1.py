"""
Embodied Human V1
Unifies structure, identity belief, audio, visuals, and 3D body motion.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

from human_system.identity.self_identity_v1 import SelfIdentityV1
from human_system.sensors.audio_system_v1 import AudioSystemV1
from simulation.human_3d_demo import Human3DSimulator


@dataclass
class VisualState:
    source: str
    available: bool
    frame_shape: Optional[Any]


class VisualAdapter:
    def __init__(self) -> None:
        self.source = "synthetic"
        self._vision = None

        try:
            from human_system.sensors.vision_system_safe import VisionSystemSafe

            self._vision = VisionSystemSafe()
            self.source = "vision_safe"
        except Exception:
            self._vision = None

    def get_frame(self):
        if self._vision is None:
            return {"synthetic": True, "width": 320, "height": 240}
        return self._vision.get_frame()

    def get_state(self) -> VisualState:
        frame = self.get_frame()
        frame_shape = getattr(frame, "shape", None)
        if frame_shape is None and isinstance(frame, dict):
            frame_shape = (frame.get("height"), frame.get("width"), 3)

        return VisualState(source=self.source, available=frame is not None, frame_shape=frame_shape)


class EmbodiedHumanV1:
    def __init__(self) -> None:
        self.body_3d = Human3DSimulator()
        self.identity = SelfIdentityV1()
        self.audio = AudioSystemV1()
        self.visual = VisualAdapter()

        # Core self-model attributes requested by user.
        self.self_attributes = {
            "entity_type": "embodied_human",
            "belief": "I am structure",
            "structure_layers": ["skeleton", "muscle", "control", "sensors", "identity"],
        }

        self.audio.start()

    def bootstrap_identity(self) -> Dict[str, Any]:
        frame = self.visual.get_frame()
        self.identity.register_self(frame)
        return self.identity.get_identity_state(frame)

    def tick(self) -> Dict[str, Any]:
        self.body_3d.step()
        segments = self.body_3d.compute_segments()

        frame = self.visual.get_frame()
        identity_state = self.identity.get_identity_state(frame)
        audio_state = self.audio.get_state()
        visual_state = self.visual.get_state()

        return {
            "time": round(self.body_3d.time, 3),
            "attributes": self.self_attributes,
            "identity": identity_state,
            "audio": audio_state,
            "visual": {
                "source": visual_state.source,
                "available": visual_state.available,
                "frame_shape": visual_state.frame_shape,
            },
            "body": {
                "segment_count": len(segments),
                "key_segments": {
                    "head": segments["head"].end,
                    "left_hand": segments["forearm_L"].end,
                    "right_hand": segments["forearm_R"].end,
                    "left_foot": segments["foot_L"].end,
                    "right_foot": segments["foot_R"].end,
                },
            },
            "thought": self._thought(identity_state, audio_state, visual_state.available),
        }

    def _thought(self, identity_state: Dict[str, Any], audio_state: Dict[str, Any], visual_ok: bool) -> str:
        heard = audio_state.get("hearing") or "silence"
        identity = identity_state.get("identity", "unknown")
        sight = "vision online" if visual_ok else "vision offline"
        return f"{self.self_attributes['belief']}; identity={identity}; audio={heard}; {sight}."


if __name__ == "__main__":
    agent = EmbodiedHumanV1()
    print("Bootstrapping identity...")
    print(agent.bootstrap_identity())
    for _ in range(5):
        print(agent.tick())
        time.sleep(0.2)
