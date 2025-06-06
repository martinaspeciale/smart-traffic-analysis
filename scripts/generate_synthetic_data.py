import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Seed per riproducibilità
random.seed(42)

# Configurazione generale
cities_config = {
    'madrid': [
        'Gran Vía', 'Calle de Alcalá', 'Paseo de la Castellana',
        'Calle de Serrano', 'Calle de Atocha', 'Calle de Goya'
    ],
    'barcelona': [
        'Passeig de Gràcia', 'Avinguda Diagonal', 'Carrer de Balmes',
        'Via Laietana', 'Gran Via de les Corts Catalanes', 'Carrer d\'Aragó'
    ],
    'london': [
        'Oxford Street', 'Regent Street', 'Piccadilly', 'Bond Street',
        'Baker Street', 'Tottenham Court Road'
    ],
    'roma': [
        'Via del Corso', 'Via Nazionale', 'Via dei Fori Imperiali',
        'Via Appia Nuova', 'Via Tuscolana', 'Via del Tritone'
    ],
    'milano': [
        'Corso Buenos Aires', 'Viale Monza', 'Corso Venezia',
        'Via Torino', 'Corso Garibaldi', 'Viale Papiniano'
    ],
    'parigi': [
        'Champs-Élysées', 'Rue de Rivoli', 'Boulevard Haussmann',
        'Avenue Montaigne', 'Rue Saint-Honoré', 'Boulevard Saint-Michel'
    ]
}

# Vehicle types possibili
vehicle_types = ['car', 'truck', 'bus', 'motorcycle']

# Parametri di generazione
start_date = (datetime.today() - timedelta(days=31)).replace(hour=0, minute=0, second=0, microsecond=0)
num_days = 30
time_interval_minutes = 15  # ogni 15 minuti

# Output dir
output_dir = 'data/raw/synthetic'
os.makedirs(output_dir, exist_ok=True)

# Funzione per generare dati per una città
def generate_city_data(city_name, streets):
    rows = []
    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        time_slots = int(24 * 60 / time_interval_minutes)
        for i in range(time_slots):
            current_time = current_date + timedelta(minutes=i * time_interval_minutes)
            for street in streets:
                row = {
                    'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'street_name': street,
                    'vehicle_count': random.randint(50, 500),
                    'vehicle_type': random.choice(vehicle_types)
                }
                rows.append(row)
    return pd.DataFrame(rows)

# Generazione per tutte le città
for city, streets in cities_config.items():
    print(f"Generating data for {city}...")
    df_city = generate_city_data(city, streets)
    output_path = os.path.join(output_dir, f"{city}.csv")
    df_city.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ Saved {len(df_city)} rows to {output_path}")

print("🎉 All synthetic datasets generated!")
