import pandas as pd
from lead_analysis import load_leads, summarize_by_category, high_value_leads


def test_summarize_by_category():
  df = load_leads('sample_leads.csv')
  summary = summarize_by_category(df)
  categories = summary.set_index('Category')['count'].to_dict()
  assert categories.get('Auto Repair') == 6


def test_high_value_leads():
  df = load_leads('sample_leads.csv')
  top = high_value_leads(df, n=1)
  assert not top.empty
