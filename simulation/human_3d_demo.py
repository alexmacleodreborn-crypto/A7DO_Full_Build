"""
A7DO 3D Human Demo

Default run exports an animated-frame OBJ mesh you can open in Blender.

Examples:
  python simulation/human_3d_demo.py
  python simulation/human_3d_demo.py --frames 240 --save-obj artifacts/human_3d.obj
  python simulation/human_3d_demo.py --frames 120 --save-frame artifacts/human_pose.png
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from human_system.joints.joint_system_v1 import JOINTS, JointSystem
from human_system.muscles.muscle_system_v1 import MUSCLES, MuscleSystem
from human_system.motion.motion_system_v2 import MotionSystemV2
from human_system.physics.biomechanics_v1 import Biomechanics

Vec3 = Tuple[float, float, float]


@dataclass
class Segment:
    name: str
    start: Vec3
    end: Vec3


def v_add(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def v_scale(a: Vec3, s: float) -> Vec3:
    return (a[0] * s, a[1] * s, a[2] * s)


class Human3DSimulator:
    def __init__(self) -> None:
        self.joint_system = JointSystem(JOINTS)
        self.muscle_system = MuscleSystem([dict(m) for m in MUSCLES])
        self.motion = MotionSystemV2(self.joint_system, self.muscle_system, Biomechanics())

        self.dt = 0.03
        self.time = 0.0

        self.lengths: Dict[str, float] = {
            "pelvis_width": 0.28,
            "spine": 0.58,
            "neck": 0.12,
            "head": 0.22,
            "clavicle": 0.17,
            "upper_arm": 0.31,
            "forearm": 0.28,
            "thigh": 0.46,
            "shin": 0.44,
            "foot": 0.24,
        }

    def _dir_from_angles(self, pitch_deg: float, yaw_deg: float = 0.0) -> Vec3:
        pitch = math.radians(pitch_deg)
        yaw = math.radians(yaw_deg)
        x = math.sin(yaw) * math.cos(pitch)
        y = -math.sin(pitch)
        z = math.cos(yaw) * math.cos(pitch)
        return (x, y, z)

    def _activate_muscles(self) -> None:
        t = self.time
        knee_ext = 0.55 + 0.45 * math.sin(2.0 * math.pi * 1.4 * t)
        knee_flex = 0.55 + 0.45 * math.sin(2.0 * math.pi * 1.4 * t + math.pi)
        hip_drive = 0.62 + 0.35 * math.sin(2.0 * math.pi * 1.4 * t + math.pi / 2.0)

        self.muscle_system.activate("quadriceps_L", knee_ext)
        self.muscle_system.activate("hamstring_L", knee_flex)
        self.muscle_system.activate("glute_L", hip_drive)
        self.muscle_system.activate("neck_stabilizer", 0.25 + 0.15 * math.sin(2 * math.pi * 0.6 * t))

    def step(self) -> None:
        self._activate_muscles()
        self.motion.step()
        self.time += self.dt

    def _left_leg_angles(self) -> Tuple[float, float]:
        hip = self.motion.get_joint_state("hip_L")["angle"]
        knee = self.motion.get_joint_state("knee_L")["angle"]
        return hip, knee

    def _right_leg_angles(self) -> Tuple[float, float]:
        t = self.time
        hip = 18.0 * math.sin(2 * math.pi * 1.4 * t + math.pi)
        knee = 30.0 + 24.0 * math.sin(2 * math.pi * 1.4 * t)
        return hip, knee

    def compute_segments(self) -> Dict[str, Segment]:
        pelvis_center = (0.0, 1.02, 0.0)
        half_pelvis = self.lengths["pelvis_width"] / 2.0

        pelvis_l = v_add(pelvis_center, (-half_pelvis, 0.0, 0.0))
        pelvis_r = v_add(pelvis_center, (+half_pelvis, 0.0, 0.0))

        spine_top = v_add(pelvis_center, (0.0, self.lengths["spine"], 0.0))
        neck = v_add(spine_top, (0.0, self.lengths["neck"], 0.0))
        head_top = v_add(neck, (0.0, self.lengths["head"], 0.0))

        shoulder_l = v_add(neck, (-self.lengths["clavicle"], 0.0, 0.0))
        shoulder_r = v_add(neck, (+self.lengths["clavicle"], 0.0, 0.0))

        arm_swing = 24.0 * math.sin(2 * math.pi * 1.4 * self.time)
        forearm_swing = 18.0 + 12.0 * math.sin(2 * math.pi * 1.4 * self.time + math.pi / 3)

        upper_dir_l = self._dir_from_angles(arm_swing, yaw_deg=-8.0)
        upper_dir_r = self._dir_from_angles(-arm_swing, yaw_deg=8.0)
        elbow_l = v_add(shoulder_l, v_scale(upper_dir_l, self.lengths["upper_arm"]))
        elbow_r = v_add(shoulder_r, v_scale(upper_dir_r, self.lengths["upper_arm"]))

        lower_dir_l = self._dir_from_angles(arm_swing + forearm_swing, yaw_deg=-8.0)
        lower_dir_r = self._dir_from_angles(-arm_swing + forearm_swing, yaw_deg=8.0)
        hand_l = v_add(elbow_l, v_scale(lower_dir_l, self.lengths["forearm"]))
        hand_r = v_add(elbow_r, v_scale(lower_dir_r, self.lengths["forearm"]))

        hip_l, knee_l = self._left_leg_angles()
        hip_r, knee_r = self._right_leg_angles()

        knee_l_pos = v_add(pelvis_l, v_scale(self._dir_from_angles(hip_l), self.lengths["thigh"]))
        knee_r_pos = v_add(pelvis_r, v_scale(self._dir_from_angles(hip_r), self.lengths["thigh"]))

        ankle_l = v_add(knee_l_pos, v_scale(self._dir_from_angles(hip_l + knee_l), self.lengths["shin"]))
        ankle_r = v_add(knee_r_pos, v_scale(self._dir_from_angles(hip_r + knee_r), self.lengths["shin"]))

        foot_l = v_add(ankle_l, v_scale(self._dir_from_angles(8.0, yaw_deg=-4.0), self.lengths["foot"]))
        foot_r = v_add(ankle_r, v_scale(self._dir_from_angles(8.0, yaw_deg=4.0), self.lengths["foot"]))

        return {
            "pelvis": Segment("pelvis", pelvis_l, pelvis_r),
            "spine": Segment("spine", pelvis_center, spine_top),
            "neck": Segment("neck", spine_top, neck),
            "head": Segment("head", neck, head_top),
            "clavicle_L": Segment("clavicle_L", neck, shoulder_l),
            "clavicle_R": Segment("clavicle_R", neck, shoulder_r),
            "upper_arm_L": Segment("upper_arm_L", shoulder_l, elbow_l),
            "upper_arm_R": Segment("upper_arm_R", shoulder_r, elbow_r),
            "forearm_L": Segment("forearm_L", elbow_l, hand_l),
            "forearm_R": Segment("forearm_R", elbow_r, hand_r),
            "thigh_L": Segment("thigh_L", pelvis_l, knee_l_pos),
            "thigh_R": Segment("thigh_R", pelvis_r, knee_r_pos),
            "shin_L": Segment("shin_L", knee_l_pos, ankle_l),
            "shin_R": Segment("shin_R", knee_r_pos, ankle_r),
            "foot_L": Segment("foot_L", ankle_l, foot_l),
            "foot_R": Segment("foot_R", ankle_r, foot_r),
        }


def export_obj(sim: Human3DSimulator, frames: int, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    vertex_index = 1
    lines: List[str] = ["# A7DO Human 3D skeleton animation frames", ""]

    for frame in range(frames):
        sim.step()
        segments = sim.compute_segments()
        lines.append(f"o frame_{frame:04d}")

        frame_vertices: List[Vec3] = []
        for seg in segments.values():
            frame_vertices.extend([seg.start, seg.end])

        for x, y, z in frame_vertices:
            lines.append(f"v {x:.6f} {y:.6f} {z:.6f}")

        for i in range(0, len(frame_vertices), 2):
            a = vertex_index + i
            b = vertex_index + i + 1
            lines.append(f"l {a} {b}")

        vertex_index += len(frame_vertices)
        lines.append("")

    output_path.write_text("\n".join(lines) + "\n")
    print(f"Saved OBJ: {output_path}")


def save_png_frame(sim: Human3DSimulator, frames: int, output_path: Path) -> None:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as exc:
        raise RuntimeError("matplotlib is required for --save-frame, but is not installed.") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    for _ in range(frames):
        sim.step()

    segments = sim.compute_segments()
    for seg in segments.values():
        xs = [seg.start[0], seg.end[0]]
        ys = [seg.start[1], seg.end[1]]
        zs = [seg.start[2], seg.end[2]]
        ax.plot(xs, zs, ys, linewidth=3)

    ax.set_title(f"A7DO 3D Human | frame={frames}")
    ax.set_xlabel("X")
    ax.set_ylabel("Z")
    ax.set_zlabel("Y")
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.8, 1.1)
    ax.set_zlim(0.0, 2.2)
    ax.view_init(elev=18, azim=28)
    plt.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Saved frame: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run A7DO full-body 3D human simulation")
    parser.add_argument("--frames", type=int, default=180, help="number of simulation frames")
    parser.add_argument("--save-obj", type=Path, default=Path("artifacts/human_3d.obj"), help="output OBJ path")
    parser.add_argument("--save-frame", type=Path, default=None, help="optional output PNG path (requires matplotlib)")
    args = parser.parse_args()

    sim = Human3DSimulator()
    export_obj(sim, frames=args.frames, output_path=args.save_obj)

    if args.save_frame:
        sim2 = Human3DSimulator()
        save_png_frame(sim2, frames=args.frames, output_path=args.save_frame)


if __name__ == "__main__":
    main()
