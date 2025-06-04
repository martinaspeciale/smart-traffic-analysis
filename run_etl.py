from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    # Change this if using .txt or .csv
    raw_file_path = "data/raw/PEMS_train.txt"
    processed_file_path = "data/processed/cleaned_PEMS_train.csv"
    db_path = "database/traffic.db"

    # Step 1: Extract
    df_raw = extract_data(raw_file_path)

    # Step 2: Transform
    df_clean = transform_data(df_raw, save_path=processed_file_path)

    # Step 3: Load into SQLite
    load_data(df_clean, db_path)

if __name__ == "__main__":
    main()

