import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("./data/anime_data.db")
# Fetch data from the database
query = "SELECT * FROM anime_data"
df = pd.read_sql(query, conn)
df = pd.read_csv("./data/MAL_data.csv")
# Close the connection
conn.close()
# Streamlit app
st.text("Hello World!")

st.dataframe(df, use_container_width=True)