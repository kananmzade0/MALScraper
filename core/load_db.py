import sqlite3
import pandas as pd
import logging
from cleaning import clean_data

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def load_to_sqlite(csv_path: str = "./data/MAL_data.csv",
                   db_path: str = "./data/anime_data.db") -> None:
    # Store the list like column names
    list_columns = ['producers', 'licensors', 'studios', 'genres', 'demographic', 'themes']

    # Load the cleaned data from the CSV file
    df = clean_data()
    print(df['genres'])

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    logging.info("Connected to SQLite database.")
    df.drop(list_columns).to_sql("anime_data", conn, if_exists="replace", index=False)
    logging.info("Loaded anime_data into SQLite database.")
    # Save the DataFrame to a SQLite table
    

    #Normalize the list-like columns
    
    for col in list_columns:
        if col in df.columns:
            exploded_df = df[['id', col]].explode(col).dropna()
            logging.info(f"Exploded {col} column.")
            logging.info(f"First row of {col} column: {exploded_df[col].iloc[0]}")
            logging.info(f"Type of the first row of {col} column: {type(exploded_df[col].iloc[0])}")
            exploded_df.to_sql(f"anime_{col}", conn, if_exists="replace", index=False)
            logging.info(f"Loaded {col} data into anime_{col} table.")

    df.to_sql("anime_genres", conn, if_exists="replace", index=False)
    # Close the connection
    conn.close()
    return None

if __name__ == "__main__":
    load_to_sqlite()