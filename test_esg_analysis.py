"""
Tests for ESG analysis script.

AI assistance: Not used — tests written by human author.
Human-reviewed by: Eric Lei
Date: 2026-03-31
"""

from pathlib import Path
from esg_analysis import load_esg_data, compute_summary


def test_load_esg_data_reads_five_endowments():
    """Verify the data file contains exactly 5 endowments."""
    data_path = Path(__file__).parent / "data" / "raw" / "endowment_esg.csv"
    scores = load_esg_data(data_path)
    assert len(scores) == 5, f"Expected 5 endowments, got {len(scores)}"


def test_compute_mean_esg_scores():
    """Verify mean calculation is correct."""
    scores = {
        "E001": [72.3, 74.1, 75.8],
        "E002": [68.5, 67.2, 69.4],
    }
    results = compute_summary(scores)
    assert results[0]["endowment_id"] == "E001"
    assert results[0]["mean_esg_score"] == round((72.3 + 74.1 + 75.8) / 3, 2)
    assert results[0]["sample_size"] == 3
    assert results[1]["endowment_id"] == "E002"
    assert results[1]["mean_esg_score"] == round((68.5 + 67.2 + 69.4) / 3, 2)
