import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/ingest.log', filemode='w')

def ingest_csv(path="./data/raw/marketData2.csv"):

    if not path:
        path = input("Enter the path to the CSV file to ingest (default: ./data/raw/marketData2.csv): ")
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logging.error(f"Error ingesting CSV file, defualt generated: {e}")
        #generate a default dataframe with the correct columns and return it
        df = pd.DataFrame(columns=['ticker', 'trade_date', 'open', 'high', 'low', 'close', 'volume'])
        return df
    