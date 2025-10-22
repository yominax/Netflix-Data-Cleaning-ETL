import logging
def load_data(df,o):
    logging.info(f"save {o}")
    df.to_csv(o,index=False)
