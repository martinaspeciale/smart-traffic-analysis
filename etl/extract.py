import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    if file_path.endswith(".csv"):
        # Standard CSV handling
        return pd.read_csv(file_path, parse_dates=['timestamp'])

    elif file_path.endswith(".txt"):
        # PeMS-specific parser
        with open(file_path, "r") as file:
            lines = file.readlines()

        data = []
        for line in lines:
            line = line.strip().strip("[]")
            parts = line.split(";")
            for part in parts:
                if part:
                    row = list(map(float, part.strip().split()))
                    data.append(row)

        df = pd.DataFrame(data)

        # Optional: save for future fast access
        df.to_csv("data/raw/PEMS_train.csv", index=False)
        return df

    else:
        raise ValueError("Unsupported file format")

