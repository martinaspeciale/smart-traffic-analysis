from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import os

def main():
    print("📊 Smart Traffic Analysis - ETL Pipeline")
    print("---------------------------------------")
    print("Available datasets:")
    print("1 - Milano (synthetic)")
    print("2 - Madrid (synthetic)")
    print("3 - Barcellona (synthetic)")
    print("4 - Londra (synthetic)")
    print("5 - Roma (synthetic)")
    print("6 - Milano (synthetic)")
    print("7 - Parigi (synthetic)")

    choice = input("Select dataset (1/2/3/4/5/6/7): ")

    if choice == '1':
        city = 'Milano'
        raw_file_path = 'data/raw/synthetic/milano.csv'
    elif choice == '2':
        city = 'Madrid'
        raw_file_path = 'data/raw/synthetic/madrid.csv'
    elif choice == '3':
        city = 'Barcellona'
        raw_file_path = 'data/raw/synthetic/barcelona.csv'
    elif choice == '4':
        city = 'Londra'
        raw_file_path = 'data/raw/synthetic/london.csv'
    elif choice == '5':
        city = 'Roma'
        raw_file_path = 'data/raw/synthetic/roma.csv'
    elif choice == '6':
        city = 'Milano fake'
        raw_file_path = 'data/raw/synthetic/milano_fake.csv'
    elif choice == '7':
        city = 'Parigi'
        raw_file_path = 'data/raw/synthetic/parigi.csv'
    else:
        print("❌ Invalid choice.")
        return

    print(f"➡️ Selected dataset: {city}")
    print(f"➡️ Loading file: {raw_file_path}")

    # Make sure processed/ directory exists
    os.makedirs('data/processed', exist_ok=True)

    # Dynamic processed file path per city
    processed_file_path = f"data/processed/cleaned_{city.lower().replace(' ', '_')}.csv"

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
