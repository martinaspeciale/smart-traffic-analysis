import pandas as pd

def extract_data(file_path, city='Milano'):
    df = pd.read_csv(file_path, sep=',')
    print(f"✅ Extracted {len(df)} rows for city: {city}")
    return df


