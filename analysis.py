"""
Inc. 5000 2014 data analysis
Usage:
  python analysis.py "Data Set- Inc5000 Company List_2014.csv"
  python analysis.py inc5000_cleaned.csv
Requires: pandas
"""
import sys
from pathlib import Path
import pandas as pd

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("inc5000_cleaned.csv")
df = pd.read_csv(path)

# Accept either the original downloaded dataset or the cleaned project CSV.
required = ["rank", "company", "industry", "state_l", "workers", "revenue", "growth"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

for col in ["rank", "workers", "revenue", "growth"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
for col in ["company", "industry", "state_l"]:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

print("=== OVERVIEW ===")
print(f"Rows: {len(df):,}")
print(f"Unique companies: {df['company'].nunique():,}")
print(f"Total workers: {df['workers'].sum():,.0f}")
print(f"Average workers/company: {df['workers'].mean():,.2f}")
print(f"Total reported revenue: ${df['revenue'].sum():,.0f}")
print(f"Median reported revenue: ${df['revenue'].median():,.0f}")
print(f"Distinct state/area labels: {df['state_l'].nunique():,}")
print(f"Median reported growth metric: {df['growth'].median():,.2f}")

state_summary = (
    df.groupby("state_l", as_index=False)
      .agg(companies=("company", "count"),
           workers=("workers", "sum"),
           revenue=("revenue", "sum"))
      .sort_values("companies", ascending=False)
)
industry_summary = (
    df.groupby("industry", as_index=False)
      .agg(companies=("company", "count"),
           workers=("workers", "sum"),
           revenue=("revenue", "sum"),
           median_growth=("growth", "median"))
      .sort_values("companies", ascending=False)
)

print("\n=== TOP 10 STATES BY COMPANY COUNT ===")
print(state_summary.head(10).to_string(index=False))
print("\n=== TOP 10 INDUSTRIES BY COMPANY COUNT ===")
print(industry_summary.head(10).to_string(index=False))
for metric, label in [("revenue", "REVENUE"), ("growth", "REPORTED GROWTH"), ("workers", "WORKFORCE")]:
    print(f"\n=== TOP 10 COMPANIES BY {label} ===")
    cols = ["rank", "company", "industry", "state_l", metric]
    print(df.nlargest(10, metric)[cols].to_string(index=False))

# Save reusable summary tables alongside the script output.
state_summary.to_csv("state_summary.csv", index=False)
industry_summary.to_csv("industry_summary.csv", index=False)
print("\nSaved state_summary.csv and industry_summary.csv")
