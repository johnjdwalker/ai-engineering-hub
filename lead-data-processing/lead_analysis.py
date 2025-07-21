import pandas as pd


from pathlib import Path


def load_leads(path: str) -> pd.DataFrame:
  file_path = Path(path)
  if not file_path.is_file():
    file_path = Path(__file__).parent / path
  return pd.read_csv(file_path)


def summarize_by_category(df: pd.DataFrame) -> pd.DataFrame:
  return df.groupby('Category').size().reset_index(name='count')


def high_value_leads(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
  if 'Value Rank' in df.columns:
    filtered = df[df['Value Rank'].str.contains('High', case=False, na=False)]
  else:
    filtered = df
  return filtered.head(n)


def main(path: str = 'sample_leads.csv'):
  df = load_leads(path)
  print('Lead count:', len(df))
  print('\nLeads by category:')
  print(summarize_by_category(df))
  print('\nTop leads:')
  print(high_value_leads(df))


if __name__ == '__main__':
  import sys
  csv_path = sys.argv[1] if len(sys.argv) > 1 else 'sample_leads.csv'
  main(csv_path)
