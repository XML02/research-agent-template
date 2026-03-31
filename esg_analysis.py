#!/usr/bin/env python3
"""
ESG Score Summary Analysis for University Endowment Funds.

Computes mean ESG scores per endowment from synthetic data.

AI assistance: Not used — code written by human author.
Human-reviewed by: Eric Lei
Date: 2026-03-31
Source: Aragon et al. (JFE 2025)

Note: This script uses equal-weighted mean aggregation per endowment.
Aragon et al. (JFE 2025) use value-weighted means (weighted by AUM).
This deviation is documented in docs/data_dictionary.md.
"""

import csv
from pathlib import Path


def load_esg_data(csv_path: Path) -> dict[str, list[float]]:
    """Load ESG scores grouped by endowment_id."""
    scores: dict[str, list[float]] = {}
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            eid = row["endowment_id"]
            score = float(row["esg_score"])
            scores.setdefault(eid, []).append(score)
    return scores


def compute_summary(scores: dict[str, list[float]]) -> list[dict]:
    """Compute mean ESG score per endowment."""
    results = []
    for eid, vals in scores.items():
        results.append({
            "endowment_id": eid,
            "mean_esg_score": round(sum(vals) / len(vals), 2),
            "sample_size": len(vals),
        })
    return sorted(results, key=lambda x: x["endowment_id"])


def save_summary(results: list[dict], output_path: Path) -> None:
    """Save summary to CSV."""
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["endowment_id", "mean_esg_score", "sample_size"])
        writer.writeheader()
        writer.writerows(results)


def main() -> int:
    data_path = Path(__file__).parent / "data" / "raw" / "endowment_esg.csv"
    output_path = Path(__file__).parent / "data" / "output" / "esg_summary.csv"
    scores = load_esg_data(data_path)
    results = compute_summary(scores)
    save_summary(results, output_path)
    print(f"Summary saved to {output_path}")
    for r in results:
        print(f"  {r['endowment_id']}: mean={r['mean_esg_score']}, n={r['sample_size']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
