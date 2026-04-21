"""
Bone Data Template (Used for all bones going forward)
Includes measurements and growth timeline
"""

BONE_TEMPLATE = {
    "id": None,
    "name": "",
    "type": "",  # long, flat, irregular, sesamoid
    "region": "",

    # Measurements (adult averages)
    "length_cm": None,
    "width_cm": None,
    "density": None,

    # Growth timeline
    "growth": {
        "prenatal": {
            "formation_week": None,
            "ossification_start": None
        },
        "birth": {
            "state": ""
        },
        "childhood": {
            "growth_rate": None
        },
        "adolescence": {
            "growth_plate_closure_age": None
        },
        "adult": {
            "final_state": "fully_ossified"
        }
    },

    # Connections placeholder
    "connects_to": [],

    # Future systems
    "muscle_attachments": [],
    "ligament_attachments": []
}
