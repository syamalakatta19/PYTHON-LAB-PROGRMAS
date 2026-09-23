# sams_json_regex.py

import json
import re
from datetime import datetime

# Regular expression patterns
EMAIL_PATTERN = r'^[\w.\-]+@[\w\-]+\.[a-zA-Z]{2,}$'
PHONE_PATTERN = r'^[6-9]\d{9}$'
ROLL_PATTERN = r'^\d{10}$'


# Sample JSON data
sample_json = '''
[
    {
        "name": "syamala katta",
        "roll_no": "2500520008",
        "email": "syamala.katta@edutech.edu",
        "phone": "7680065111"
    },
    {
        "name": "Zoya Khan",
        "roll_no": "SAMS24CS099",
        "email": "bad-email",
        "phone": "12345"
    }
]
'''


# Convert JSON text into Python objects
def parse_admissions(json_text):
    return json.loads(json_text)


# Validate student record
def validate_record(record):
    return {
        "name": record["name"],
        "roll_no_valid": bool(
            re.match(ROLL_PATTERN, record["roll_no"])
        ),
        "email_valid": bool(
            re.match(EMAIL_PATTERN, record["email"])
        ),
        "phone_valid": bool(
            re.match(PHONE_PATTERN, record["phone"])
        ),
        "imported_at": datetime.now().isoformat(timespec="seconds")
    }


# Main program
if __name__ == "__main__":

    records = parse_admissions(sample_json)

    print("=== SAMS External Data Validation ===")

    for r in records:
        result = validate_record(r)
        print(result)