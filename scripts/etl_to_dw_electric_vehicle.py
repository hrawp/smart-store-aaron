import pandas as pd
import sqlite3
import pathlib
import sys

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
DW_DIR: pathlib.Path = DATA_DIR.joinpath("dw")
DB_PATH: pathlib.Path = DW_DIR.joinpath("electric_vehicle.db")
PREPARED_DATA_DIR : pathlib.Path = DATA_DIR.joinpath("prepared")



# Ensure the 'data/dw' directory exists
DW_DIR.mkdir(parents=True, exist_ok=True)
def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS electric_vehicle (
            unique_code INTEGER PRIMARY KEY,
            vin TEXT,
            county TEXT,
            city TEXT,
            state TEXT,
            postal_code TEXT,
            model_year INTEGER,
            make TEXT,
            model TEXT,
            electric_vehicle_type TEXT,
            cafv_eligibility TEXT,
            electric_range INTEGER,                 
            base_msrp INTEGER,
            dol_vehicle_id INTEGER, 
            vehicle_location TEXT,
            electric_utility TEXT        
        )
    """)
    

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    """Delete all existing records from the electric_vehicle table."""
    cursor.execute("DELETE FROM electric_vehicle")


def insert_electric_vehicles(electric_vehicles_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert electric_vehicle data into the electric_vehicle table."""
    electric_vehicles_df.to_sql("electric_vehicle", cursor.connection, if_exists="append", index=False)



def load_data_to_db() -> None:
    try:
        # Connect to SQLite – will create the file if it doesn't exist
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create schema and clear existing records
        create_schema(cursor)
        delete_existing_records(cursor)

        # Load prepared data using pandas
        electric_vehicles_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("electric_vehicle.csv"))


        # Insert data into the database
        insert_electric_vehicles(electric_vehicles_df, cursor)


        conn.commit()
    finally:
        if conn :
            conn.close()

if __name__ == "__main__":
    load_data_to_db()