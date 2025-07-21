# Lead Data Processing

This example shows how to analyze CSV lead data using **pandas**. The script summarizes records by category and lists high‑value leads when a `Value Rank` column is present.

## Installation

Install the required library:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with a CSV file path (defaults to `sample_leads.csv`):

```bash
python3 lead_analysis.py [path/to/leads.csv]
```

The output includes the total lead count, a table of counts per category and the first few high‑value leads.
