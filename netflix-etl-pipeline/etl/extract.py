import pandas as pd
import logging
def extract_data(p):
    logging.info(f"extract {p}")
    df = pd.read_csv(p)
    return df
