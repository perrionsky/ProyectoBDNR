import pydgraph
import pandas as pd

def set_schema(client):
    schema = """
    name: string @index(exact) .
    url: string .
    query: string .
    tweet_volume: int .
    searched_at_datetime: datetime .
    searched_in_country: string @index(term) .
    """
    op = pydgraph.Operation(schema=schema)
    client.alter(op)

def add_trend(client, trend_data):
    txn = client.txn()
    try:
        response = txn.mutate(set_obj=trend_data)
        txn.commit()
        return response
    finally:
        txn.discard()

def search_trends_by_country(client, country):
    query = f"""
    {{
        trends(func: eq(searched_in_country, "{country}")) {{
            uid
            name
            url
            query
            tweet_volume
            searched_at_datetime
            searched_in_country
        }}
    }}
    """
    txn = client.txn(read_only=True)
    try:
        res = txn.query(query)
        return res.json
    finally:
        txn.discard()


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
