import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

inp="data/netflix_titles.csv"
out="output/cleaned_netflix.csv"

def run():
    logging.info("start etl")
    df=extract_data(inp)
    df2=transform_data(df)
    load_data(df2,out)
    logging.info("done")

if __name__=="__main__":
    run()
