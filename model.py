import pydgraph
import pandas as pd

def load_data(filepath):
    return pd.read_json(filepath)

def search_trend(df, name):
    return df[df['trend_name'].str.contains(name, case=False, na=False)]

def search_trend_by_country(df, country):
    return df[df['searched_in_country'].str.contains(country, case=False, na=False)]

def add_trend(df, trend_data):
    return df.append(trend_data, ignore_index=True)

def delete_trend(df, name):
    return df[~df['trend_name'].str.contains(name, case=False, na=False)]

def save_data(df, filepath):
    df.to_json(filepath, orient='records', date_format='iso')
