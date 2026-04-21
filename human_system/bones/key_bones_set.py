"""
Key Bones Set (Phase 1 Upgrade)
Includes femur, skull, spine (simplified), pelvis
All follow enhanced template with measurements + growth timeline
"""

FEMUR_L = {
    "id": 1,
    "name": "femur_L",
    "type": "long",
    "region": "lower_limb",

    "length_cm": 48,
    "width_cm": 3.5,
    "density": 1.85,

    "growth": {
        "prenatal": {"formation_week": 7, "ossification_start": 8},
        "birth": {"state": "partially ossified"},
        "childhood": {"growth_rate": "high"},
        "adolescence": {"growth_plate_closure_age": 16},
        "adult": {"final_state": "fully_ossified"}
    },

    "connects_to": ["pelvis", "tibia"],
    "muscle_attachments": [],
    "ligament_attachments": []
}

SKULL = {
    "id": 2,
    "name": "skull",
    "type": "flat",
    "region": "head",

    "length_cm": 22,
    "width_cm": 15,
    "density": 1.6,

    "growth": {
        "prenatal": {"formation_week": 4, "ossification_start": 8},
        "birth": {"state": "fontanelles open"},
        "childhood": {"growth_rate": "moderate"},
        "adolescence": {"growth_plate_closure_age": 18},
        "adult": {"final_state": "fused plates"}
    },

    "connects_to": ["spine"],
    "muscle_attachments": [],
    "ligament_attachments": []
}

SPINE = {
    "id": 3,
    "name": "spine",
    "type": "irregular",
    "region": "axial",

    "length_cm": 70,
    "width_cm": 5,
    "density": 1.8,

    "growth": {
        "prenatal": {"formation_week": 4, "ossification_start": 9},
        "birth": {"state": "segmented"},
        "childhood": {"growth_rate": "moderate"},
        "adolescence": {"growth_plate_closure_age": 20},
        "adult": {"final_state": "fully segmented"}
    },

    "connects_to": ["skull", "pelvis"],
    "muscle_attachments": [],
    "ligament_attachments": []
}

PELVIS = {
    "id": 4,
    "name": "pelvis",
    "type": "irregular",
    "region": "core",

    "length_cm": 28,
    "width_cm": 30,
    "density": 1.9,

    "growth": {
        "prenatal": {"formation_week": 6, "ossification_start": 9},
        "birth": {"state": "multi-part"},
        "childhood": {"growth_rate": "moderate"},
        "adolescence": {"growth_plate_closure_age": 18},
        "adult": {"final_state": "fused"}
    },

    "connects_to": ["spine", "femur_L", "femur_R"],
    "muscle_attachments": [],
    "ligament_attachments": []
}
