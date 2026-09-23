"""
Compare 12-month weight loss between the standard and intensive program tracks.

Weight loss is defined as weight_baseline_kg - weight_12m_kg. Patients with a
missing weight_12m_kg dropped out before completing the program and are
excluded from the comparison.
"""

import sys
from typing import cast

import pandas as pd
from scipy import stats


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <data_file.csv>")
        sys.exit(1)

    data_path = sys.argv[1]
    df = pd.read_csv(data_path)

    completed = df.dropna(subset=["weight_12m_kg"]).copy()
    completed["weight_loss_kg"] = (
        completed["weight_baseline_kg"] - completed["weight_12m_kg"]
    )

    standard = completed.loc[completed["track"] == "standard", "weight_loss_kg"]
    intensive = completed.loc[completed["track"] == "intensive", "weight_loss_kg"]

    n_dropped = len(df) - len(completed)
    print(f"Total patients: {len(df)}")
    print(f"Excluded (dropped out, missing weight_12m_kg): {n_dropped}")
    print(f"Completed - standard track: n={len(standard)}, "
          f"mean weight loss={standard.mean():.2f} kg, sd={standard.std():.2f} kg")
    print(f"Completed - intensive track: n={len(intensive)}, "
          f"mean weight loss={intensive.mean():.2f} kg, sd={intensive.std():.2f} kg")

    t_stat, p_value = stats.ttest_ind(intensive, standard, equal_var=False)
    t_stat = cast(float, t_stat)
    p_value = cast(float, p_value)
    print()
    print("Welch's t-test (intensive vs. standard weight loss):")
    print(f"  t = {t_stat:.3f}")
    print(f"  p = {p_value:.4g}")

    alpha = 0.05
    if p_value < alpha:
        print(f"  -> Statistically significant difference at alpha={alpha}.")
    else:
        print(f"  -> No statistically significant difference at alpha={alpha}.")


if __name__ == "__main__":
    main()
