import sqlite3
import pandas as pd

pd.read_json('data/anime_list.json').to_sql('anime_list', sqlite3.connect('data/anime_list.db'))