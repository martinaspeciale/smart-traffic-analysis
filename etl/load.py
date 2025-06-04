
import sqlite3

def load_data(df, db_path: str):
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql("traffic_data", conn, if_exists="replace", index=False)
        conn.close()
        print(f"✅ Data loaded into {db_path}")
    except Exception as e:
        print(f"❌ Loading error: {e}")
