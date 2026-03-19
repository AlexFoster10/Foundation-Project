import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/output.log', filemode='w')   

def output_csv(df, path="./data/processed/processed_data.csv"):

    if not path:
        path = input("Enter the path to save the output CSV file (default: ./data/processed/processed_data.csv): ")

    try:
        df.to_csv(path)
    except Exception as e:
        logging.error(f"Error outputting CSV file: {e}")



