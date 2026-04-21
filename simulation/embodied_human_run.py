"""
Run an integrated embodied human loop with 3D body, identity, audio and visual states.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from human_system.integration.embodied_human_v1 import EmbodiedHumanV1
from simulation.human_3d_demo import export_obj


def main() -> None:
    parser = argparse.ArgumentParser(description="A7DO integrated embodied human run")
    parser.add_argument("--steps", type=int, default=20, help="number of update ticks")
    parser.add_argument("--interval", type=float, default=0.15, help="seconds between ticks")
    parser.add_argument("--save-log", type=Path, default=Path("artifacts/embodied_human_state.json"), help="state output path")
    parser.add_argument("--save-obj", type=Path, default=Path("artifacts/human_3d.obj"), help="3D body OBJ output")
    args = parser.parse_args()

    agent = EmbodiedHumanV1()
    identity = agent.bootstrap_identity()

    states = [{"boot_identity": identity}]
    for _ in range(args.steps):
        states.append(agent.tick())
        time.sleep(args.interval)

    args.save_log.parent.mkdir(parents=True, exist_ok=True)
    args.save_log.write_text(json.dumps(states, indent=2))

    # Export an aligned 3D animation clip of the same duration.
    export_obj(agent.body_3d, frames=args.steps, output_path=args.save_obj)

    print(f"Saved state log: {args.save_log}")
    print(f"Saved body OBJ: {args.save_obj}")


if __name__ == "__main__":
    main()
