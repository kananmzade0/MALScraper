import pandas as pd
import logging
# Initlal import of data
def import_data():
    df1 = pd.read_json("./data/anime_full_details.json")
    df2 = pd.read_json("./data/anime_list.json")
    return df1, df2

def add_id_column()-> tuple[pd.DataFrame, pd.DataFrame]:
    df1, df2 = import_data()
    df1['id'] = df1['link'].apply(lambda x: x.split("/anime/")[1].split("/")[0] if isinstance(x, str) and "/anime/" in x else None)
    df2['id'] = df2['link'].apply(lambda x: x.split("/anime/")[1].split("/")[0] if isinstance(x, str) and "/anime/" in x else None)
    return df1, df2

def merge_dataframes() -> pd.DataFrame:
    df1, df2 = add_id_column()

    df_merged = pd.merge(left=df1, 
                         right=df2, 
                         how='right', 
                         on=['id'], 
                         suffixes=(None, '_y'))
    
    return df_merged

# Cleaning part starts here
def clean_list_like_columns(df: pd.DataFrame) -> pd.DataFrame:  # TODO: Write tests to check if list_like columns are exactly same as in the comment above
    
    replace_words = ['add some', '']

    def fetch_list_like_columns(df: pd.DataFrame) -> list:
        list_like_columns = []
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, list)).any():
                list_like_columns.append(col)
        return list_like_columns # Should be ['producers', 'licensors', 'studios', 'genres', 'demographic', 'themes']

    def is_junk_list(x: list) -> bool:
        return isinstance(x, list) and all(
            str(i).strip().lower() in replace_words for i in x
        )          
    
    list_like_columns = fetch_list_like_columns(df)

    for col in list_like_columns:
        df[col] = df[col].apply(lambda x: pd.NA if is_junk_list(x) else x)  

    df['broadcast'] = df['broadcast'].explode()

    return df
def replace_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    for i in df.columns:
        df[i] = df[i].apply(lambda x: x.replace("\n", "") if isinstance(x, str) else x)
    return df

def change_types(df: pd.DataFrame) -> pd.DataFrame:
    change_types = ['episodes', 'ranked', 'popularity', 'members', 'favorites', 'id', 'rank']
    for i in change_types:
        df[i] = df[i].str.replace("#", "").str.replace(",", "")
        df[i] = pd.to_numeric(df[i], errors="coerce") # coerce means that if it can't convert it, it will set it to NaN
    return df

def clean_data(df: pd.DataFrame = None,
               save: bool = True) -> pd.DataFrame:
    df = merge_dataframes()
    df = df.drop_duplicates(subset=['id'])
    df = replace_whitespace(df)
    df = change_types(df)
    df = clean_list_like_columns(df)

    if save:
        df.to_csv("./data/MAL_data.csv", index=False)
        logging.info("Clean data saved to CSV file.")

    return df

if __name__ == "__main__":
    # Example usage
    # Assuming you have already run the spiders and have the JSON files
    clean_data()