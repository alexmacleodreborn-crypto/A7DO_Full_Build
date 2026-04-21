# A7DO Full Build

A7DO is a full-stack artificial life and intelligence system built from first principles:

- Skeletal system
- Muscle system
- Neural control
- Environment interaction

## Structure

A7DO_Full_Build/
├── core/
├── body/
├── brain/
├── world/
├── simulation/
└── main.py

This repository builds toward a fully embodied AI system.

## 3D Human Simulation

You can now run a full-body 3D articulated human skeleton simulation driven by the repo's joint, muscle, and biomechanics systems.

```bash
python simulation/human_3d_demo.py --frames 240 --save-obj artifacts/human_3d.obj
```

Optional PNG snapshot export (requires matplotlib):

```bash
python simulation/human_3d_demo.py --frames 120 --save-frame artifacts/human_pose.png
```

## Embodied Human (Structure + Audio + Visual)

This integrated run wires everything together so you can inspect:
- the agent's self-attribute belief (`"I am structure"`),
- identity state,
- audio sensing state,
- visual sensing state,
- and synchronized 3D body output.

```bash
python simulation/embodied_human_run.py --steps 30
```

Outputs:
- `artifacts/embodied_human_state.json` (attributes, thoughts, audio/visual state, body key points)
- `artifacts/human_3d.obj` (3D skeleton frames)

