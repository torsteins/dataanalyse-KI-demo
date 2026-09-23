"""Generate dummy patient data matching data_description.md."""

import csv
import random
from datetime import date, timedelta

NUM_ENTRIES = 1000
OUTPUT_PATH = "dummy_data.csv"

TRACKS = ["standard", "intensive"]
SEXES = ["F", "M"]
MUNICIPALITY_CODES = ["4601", "0301", "5001", "1103", "4204", "3001", "1806"]
NOTES = ["", "", "", "referred by GP", "follow-up needed", "relocated mid-program"]

MIN_ENROLMENT_AGE = 18
MAX_ENROLMENT_AGE = 75
DROPOUT_RATE = 0.2


def random_date(start: date, end: date) -> date:
    delta_days = (end - start).days
    return start + timedelta(days=random.randint(0, delta_days))


def generate_person(patient_id: int) -> dict:
    enrolment_date = random_date(date(2020, 1, 1), date(2023, 12, 31))
    age_at_enrolment = random.randint(MIN_ENROLMENT_AGE, MAX_ENROLMENT_AGE)
    birth_date = enrolment_date.replace(year=enrolment_date.year - age_at_enrolment)

    sex = random.choice(SEXES)
    height_cm = round(random.gauss(165 if sex == "F" else 179, 7), 1)
    weight_baseline_kg = round(random.gauss(95, 15), 1)

    completed_program = random.random() > DROPOUT_RATE
    if completed_program:
        weight_change_kg = random.gauss(-6, 5)
        weight_12m_kg = round(max(weight_baseline_kg + weight_change_kg, 40), 1)
    else:
        weight_12m_kg = ""

    return {
        "patient_pseudonym": f"P{patient_id:05d}",
        "birth_date": birth_date.isoformat(),
        "sex": sex,
        "municipality_code": random.choice(MUNICIPALITY_CODES),
        "enrolment_date": enrolment_date.isoformat(),
        "age_at_enrolment": age_at_enrolment,
        "height_cm": height_cm,
        "track": random.choice(TRACKS),
        "weight_baseline_kg": weight_baseline_kg,
        "weight_12m_kg": weight_12m_kg,
        "note": random.choice(NOTES),
    }


def generate_dataset(n: int) -> list[dict]:
    return [generate_person(i + 1) for i in range(n)]


def main() -> None:
    rows = generate_dataset(NUM_ENTRIES)
    fieldnames = list(rows[0].keys())

    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
