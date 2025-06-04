
# Smart Traffic Analysis System

This project analyzes urban traffic congestion using real-world sensor data. It includes:

- ✅ ETL pipeline using SQLite
- ✅ Clustering to detect congestion patterns
- ✅ Time series modeling to forecast traffic
- ✅ Interactive dashboard with Streamlit

## How to Run

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the dashboard:
   ```
   streamlit run dashboard/app.py
   ```

## Project Structure

- `etl/`: Data extraction, transformation, loading scripts
- `analysis/`: Modeling and clustering logic
- `dashboard/`: Streamlit app
- `database/`: Contains SQLite DB (traffic.db)
- `data/`: Raw and processed data

---

Author: Martina Speciale
