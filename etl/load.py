import sqlite3

def load_data(df, db_path: str):
    try:
        # Check if 'city_name' column exists
        if 'city_name' not in df.columns:
            print("⚠️ Warning: 'city_name' column not found in dataframe. Adding default 'Unknown'.")
            df['city_name'] = 'Unknown'

        conn = sqlite3.connect(db_path)

        # Important: use 'append' to support multi-city
        df.to_sql("traffic_data", conn, if_exists="append", index=False)

        conn.close()
        print(f"✅ Data loaded into {db_path} ({len(df)} rows)")
    except Exception as e:
        print(f"❌ Loading error: {e}")
