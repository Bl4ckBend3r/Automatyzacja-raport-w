import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['quantity'] * df['price']
    return df

def summarize(df):
    summary = df.groupby('region', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
    return summary
