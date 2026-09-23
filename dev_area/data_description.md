# Data Description

This dataset tracks patients enrolled in a weight management program.

## Columns

| Column               | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| `patient_pseudonym`  | Pseudonymized patient identifier.                                                              |
| `birth_date`         | Patient's date of birth.                                                                        |
| `sex`                | Patient's sex.                                                                                  |
| `municipality_code`  | Code identifying the patient's municipality.                                                    |
| `enrolment_date`     | Date the patient enrolled in the program.                                                       |
| `age_at_enrolment`   | Patient's age at the time of enrolment.                                                         |
| `height_cm`          | Patient's height in centimeters.                                                                 |
| `track`              | Program track the patient was assigned to: either `standard` or `intensive`.                    |
| `weight_baseline_kg` | Patient's weight (kg) at baseline, i.e. at enrolment.                                            |
| `weight_12m_kg`      | Patient's weight (kg) at 12 months. May be blank for patients who did not complete the full program. |
| `note`               | Free-text note field.                                                                            |

## Notes

- The `track` column has exactly two possible values: `standard` and `intensive`.
- Missing values in `weight_12m_kg` indicate patients who dropped out before completing the full 12-month program, rather than a data entry error.
