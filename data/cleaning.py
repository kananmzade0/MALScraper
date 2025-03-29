import pandas as pd

def clean_data():
    df1 = pd.read_json("anime_full_details.json")
    df2 = pd.read_json("anime_list.json")

    df1['id'] = df1['link'].apply(lambda x: x.split("/anime/")[1].split("/")[0] if isinstance(x, str) and "/anime/" in x else None)
    df2['id'] = df2['link'].apply(lambda x: x.split("/anime/")[1].split("/")[0] if isinstance(x, str) and "/anime/" in x else None)

    df_merged = pd.merge(left=df1, right=df2, how='right', on=['id'], suffixes=(None, '_y'))
    df_merged = df_merged.drop(columns=['title_y', 'link_y', 'score_y']) # drop duplicate columns that were added by the merge

    df_merged = df_merged.drop_duplicates(subset=['id'])

    df_merged['broadcast'] = df_merged['broadcast'].explode()

    for i in df_merged.columns:
        df_merged[i] = df_merged[i].apply(lambda x: x.replace("\n", "") if isinstance(x, str) else x)

    return df_merged