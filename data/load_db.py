import sqlite3
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def load_to_sqlite(csv_path: str = "./data/MAL_data.csv",
                   db_path: str = "./data/anime_data.db") -> None:
    # Load the cleaned data from the CSV file
    df = pd.read_csv(csv_path)
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    # Save the DataFrame to a SQLite table
    df.to_sql("anime_data", conn, if_exists="replace", index=False)

    #Normalize the list-like columns
    list_columns = ['producers', 'licensors', 'studios', 'genres', 'demographic', 'themes']
    for col in list_columns:
        if col in df.columns:
            exploded_df = df[['id', col]].explode(col).dropna()
            exploded_df.to_sql(f"anime_{col}", conn, if_exists="replace", index=False)
            logging.info(f"Loaded {col} data into anime_{col} table.")

    # Close the connection
    conn.close()
    return None

if __name__ == "__main__":
    load_to_sqlite()