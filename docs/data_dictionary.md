# Data Dictionary — Endowment ESG Scores

## Source
This data is used for reproducing aspects of:
> Aragon, George O., Yuxiang Jiang, Juha Joenväärä, and Cristian Ioan Tiu. 2025. "Responsible Investing: Costs and Benefits for University Endowment Funds." *Journal of Financial Economics*, 172:104151.

## Note on Data
Real endowment ESG data is proprietary. This file contains **synthetic data** (15 rows, 5 endowments × 3 years) for demonstration purposes only. Synthetic endowments are labeled E001–E005.

## Variables

| Variable | Type | Description | Range |
|----------|------|-------------|-------|
| `endowment_id` | string | Unique identifier for each university endowment fund | E001–E005 |
| `year` | integer | Calendar year of the ESG score observation | 2022–2024 |
| `esg_score` | float | ESG performance score (0–100 scale, higher is better) | 65.3–82.7 |

## Methodology

### ESG Score Aggregation
This project uses **equal-weighted mean** ESG scores per endowment:
```
mean_esg_score = Σ(esg_score_year) / n_years
```
For example, E001: (72.3 + 74.1 + 75.8) / 3 = 74.07

### Deviation from Aragon et al. (JFE 2025)
Aragon et al. use **value-weighted means**, weighting by assets under management (AUM):
```
value_weighted_mean = Σ(esg_score_i × AUM_i) / Σ(AUM_i)
```

We use equal-weighted means because AUM data is proprietary and unavailable for synthetic endowments. This deviation is documented to ensure reproducibility and honest reporting.

## Limitations
1. Synthetic data is not representative of real endowment ESG distributions
2. Equal weighting underweights large endowments relative to Aragon et al.'s methodology
3. External validity is limited — results should not be generalized to real endowments
4. Only 5 endowments × 3 years — small sample limits statistical power

## File Locations
- Raw data: `data/raw/endowment_esg.csv`
- Summary output: `data/output/esg_summary.csv`
- Analysis script: `esg_analysis.py`
- Tests: `test_esg_analysis.py`

## Verification Commands
```bash
# Verify row count
python -c "import csv; r=list(csv.DictReader(open('data/raw/endowment_esg.csv'))); print(f'Rows: {len(r)}, Columns: {list(r[0].keys())}')"
# Expected: Rows: 15, Columns: ['endowment_id', 'year', 'esg_score']

# Run analysis and tests
python esg_analysis.py && pytest test_esg_analysis.py -v
# Expected: 2 passed in 0.01s
```
