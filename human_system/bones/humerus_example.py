"""
Example Bone: Humerus (Left)
"""

HUMERUS_L = {
    "id": 85,
    "name": "humerus_L",
    "type": "long",
    "region": "upper_limb",

    # Measurements (approx adult averages)
    "length_cm": 30,
    "width_cm": 2.5,
    "density": 1.85,

    "growth": {
        "prenatal": {
            "formation_week": 7,
            "ossification_start": 8
        },
        "birth": {
            "state": "partially ossified"
        },
        "childhood": {
            "growth_rate": "high"
        },
        "adolescence": {
            "growth_plate_closure_age": 16
        },
        "adult": {
            "final_state": "fully_ossified"
        }
    },

    "connects_to": [83, 87, 89],  # scapula, radius, ulna

    "muscle_attachments": [],
    "ligament_attachments": []
}
