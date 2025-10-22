import pandas as pd
import logging
def transform_data(df):
    logging.info("transform")
    df=df.drop_duplicates()
    df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
    df['rating']=df['rating'].fillna('Unknown')
    for c in ['cast','listed_in']:
        df[c]=df[c].fillna('').apply(lambda x:[i.strip() for i in x.split(',') if i])
    df['duration_minutes']=df['duration'].fillna('').apply(lambda x:int(x.split()[0]) if 'min' in x else None)
    return df
