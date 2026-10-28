# US Company Growth & Workforce Analysis (Inc. 5000, 2014)

## Project overview
This beginner-friendly data analytics project explores the 2014 Inc. 5000 company list. It uses company rank, industry, location, workforce size, reported revenue, reported growth, and years on the list to identify geographic and industry patterns.

## Business questions
1. How many companies are included, and how many workers do they report?
2. Which states have the most listed companies?
3. Which industries have the most companies?
4. Which companies have the highest reported revenue, growth, and workforce?
5. How do reported revenue and growth vary across the listed companies?

## Tools
- Python (pandas) for cleaning and analysis
- Excel-compatible workbook for summary tables and charts
- CSV for cleaned data
- Google Sheets can also be used to inspect the cleaned CSV

## Files
- `Inc5000_Data_Analyst_Project.xlsx` — dashboard, cleaned data, state and industry summaries, and top-company tables.
- `inc5000_cleaned.csv` — cleaned analytical data with 5,000 rows.
- `analysis.py` — reproducible analysis script.
- `README.md` — project documentation.

## Highlights from the dataset
- Companies: **5,000**
- Distinct company names: **5,000**
- Total reported workers: **1,044,849**
- Average reported workers per company: **208.97**
- Total reported revenue: **$215.29 billion**
- Median reported revenue per company: **$10.72 million**
- Distinct state/area labels: **51**
- Largest state by company count: **California (694)**
- Next states by company count: **Texas (404)** and **New York (335)**
- Largest industry by company count: **IT Services (733)**

## Interpretation notes
- The source is a 2014 snapshot; it should not be presented as current market data.
- The dataset's `growth` field is retained as provided by the source. It is treated as a reported growth metric; this project does not independently validate the source's calculation period or methodology.
- `state_l` contains 51 distinct labels. This may include a non-state/territory label, so the metric is described as distinct state/area labels rather than asserting 51 US states.
- Total revenue is the sum of reported revenue across the listed companies. It is not an estimate of the entire US economy.
- Rankings and correlations are descriptive, not proof of causation.

## How to run the Python analysis
Install dependencies:
```bash
pip install pandas
```
Run:
```bash
python analysis.py "Data Set- Inc5000 Company List_2014.csv"
```
If you downloaded only the project bundle, you can also run it against `inc5000_cleaned.csv`:
```bash
python analysis.py inc5000_cleaned.csv
```

## Suggested interview explanation
“I analyzed the 2014 Inc. 5000 company dataset using Python and spreadsheet dashboards. I cleaned the relevant columns, checked missing values, and grouped the companies by state and industry. I summarized workforce and revenue, compared top companies by revenue, reported growth, and workforce, and visualized the states and industries with the most listed companies. The analysis showed California had the highest company count and IT Services was the largest industry by company count. I also documented the limitations of using a historical snapshot and source-reported growth values.”

## Data source
The uploaded file was titled `Data Set- Inc5000 Company List_2014.csv` and contains a source URL field referencing Inc.com's 2014 Inc. 5000 list JSON. Cite the original source if redistributing the dataset publicly.
