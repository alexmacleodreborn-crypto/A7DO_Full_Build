# A7DO Human System — Architecture Map (v1)

This document maps the current repository to the intended biological engine architecture.

---

## 1. STRUCTURE LAYER (Bones)
**Folder:** `human_system/bones/`

Represents rigid body components.

- skull.py
- spine.py
- upper_limbs.py
- lower_limbs.py
- key_bones_set.py
- _bone_template.py

**Status:** ✅ Implemented (partial detail)

---

## 2. JOINT LAYER (Connections)
**Folder:** `human_system/joints/`

Defines how bones connect and move.

- joint_system_v1.py

**Includes:**
- Joint types (hinge, ball, pivot)
- Movement ranges

**Status:** ✅ Implemented (basic)

---

## 3. MUSCLE LAYER (Force Generation)
**Folder:** `human_system/muscles/`

Defines how force is applied.

- muscle_system_v1.py

**Includes:**
- Muscle definitions
- Activation system
- Joint force output

**Status:** ✅ Implemented (simplified)

---

## 4. DYNAMICS LAYER (Physics)
**Folder:**
- `human_system/physics/`
- `human_system/motion/`

**Files:**
- biomechanics_v1.py
- motion_system_v1.py
- motion_system_v2.py

**Includes:**
- Torque
- Inertia
- Damping
- Angular motion

**Status:** ✅ Implemented (core physics working)

---

## 5. KINEMATICS LAYER (Geometry)
**Folder:** `human_system/motion/`

- forward_kinematics_v1.py

**Includes:**
- Joint angles → spatial positions

**Status:** ✅ Implemented (partial body)

---

## 6. NEURAL LAYER (Control)
**Folder:** `human_system/neural/`

- neural_system_v1.py

**Includes:**
- Signal latency
- Muscle activation delay
- PID controller (not yet integrated)

**Status:** ⚠️ Partial (no feedback loop yet)

---

## 7. MISSING SYSTEMS (Critical Next Steps)

### ❌ Balance System
- Center of Mass (CoM)
- Ground contact
- Stability

### ❌ Neural Feedback Loop
- Proprioception
- Reflexes
- Closed-loop control

### ❌ Strength Curves
- Torque varies with angle

### ❌ Full Body Chain
- Arms
- Both legs
- Hierarchical transforms

---

## CURRENT STATE SUMMARY

```
Structure ✔
Joints ✔
Muscles ✔
Dynamics ✔
Kinematics ✔
Neural ⚠️
Control ❌
Behaviour ❌
```

---

## KEY INSIGHT

This is NOT an animation system.

This is a:

> Physics-based biomechanical human engine

Movement is **emergent**, not scripted.

---

## NEXT PRIORITY

1. Neural Feedback Loop
2. Balance System (CoM)
3. Strength Curves
4. Full Body Kinematics

---

End of document.
