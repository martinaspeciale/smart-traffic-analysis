
import pandas as pd
import os

def transform_data(df: pd.DataFrame, save_path: str = None) -> pd.DataFrame:
    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by=['timestamp', 'location'])

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            df.to_csv(save_path, index=False)
            print(f"✅ Processed data saved to: {save_path}")

        print(f"✅ Data transformed. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Transformation error: {e}")
        return pd.DataFrame()
