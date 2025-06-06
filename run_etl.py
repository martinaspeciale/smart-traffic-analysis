from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import os

def main():
    print("📊 Smart Traffic Analysis - ETL Pipeline")
    print("---------------------------------------")
    print("Available datasets:")
    print("1 - Milano (2015)")
    print("2 - Londra")

    choice = input("Select dataset (1/2): ")

    if choice == '1':
        city = 'Milano'
        raw_file_path = 'data/raw/milano.csv'
    elif choice == '2':
        city = 'Londra'
        raw_file_path = 'data/raw/london.csv'
    else:
        print("❌ Invalid choice.")
        return

    print(f"➡️ Selected dataset: {city}")
    print(f"➡️ Loading file: {raw_file_path}")

    # Make sure processed/ directory exists
    os.makedirs('data/processed', exist_ok=True)

    # Dynamic processed file path per city
    processed_file_path = f"data/processed/cleaned_{city.lower()}.csv"

    # Database path
    db_path = "database/traffic.db"

    # Step 1: Extract
    try:
        df_raw = extract_data(raw_file_path, city=city)
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return

    # Step 2: Transform
    try:
        df_clean = transform_data(df_raw, city=city, save_path=processed_file_path)
    except Exception as e:
        print(f"❌ Transformation error: {e}")
        return

    # Step 3: Load into SQLite
    try:
        load_data(df_clean, db_path)
    except Exception as e:
        print(f"❌ Loading error: {e}")
        return

    print(f"✅ ETL pipeline completed successfully for {city}.")

if __name__ == "__main__":
    main()
