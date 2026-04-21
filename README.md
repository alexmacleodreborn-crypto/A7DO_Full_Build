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

