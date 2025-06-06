
import pandas as pd
import os

def transform_data(df_raw, city='Milano', save_path=None):
    print(f"🔄 Transforming data for {city}...")
    df = pd.DataFrame()

    if city in ['Milano', 'Madrid', 'Barcellona', 'Londra', 'Roma', 'Milano fake', 'Parigi']:
        # In tutti i synthetic dataset, i CSV hanno già la struttura corretta:
        # timestamp, street_name, vehicle_count, vehicle_type
        df['timestamp'] = pd.to_datetime(df_raw['timestamp'], errors='coerce')
        df['street_name'] = df_raw['street_name']
        df['vehicle_count'] = pd.to_numeric(df_raw['vehicle_count'], errors='coerce')
        df['vehicle_type'] = df_raw['vehicle_type']
        df['city_name'] = city

    else:
        raise ValueError(f"🚫 Unsupported city: {city}")

    # Pulizia → rimuovo eventuali righe con NaN
    df.dropna(inplace=True)

    # Save processed data if requested
    if save_path:
        df.to_csv(save_path, index=False)
        print(f"✅ Processed data saved to {save_path}")

    print(f"✅ Transformed {len(df)} rows for {city}.")
    return df
