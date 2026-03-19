import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tests/logs/processing.log', filemode='w')

def daily_return(df):
    try:
        df['daily_return'] = (df['close'] - df['open']) / df['open']
        return df
    except Exception as e:
        logging.error(f"Error calculating daily return: {e}")
        df['daily_return'] = np.nan
        return df
    
def price_spread(df):
    try:
        df['price_spread'] = df['high'] - df['low']
        return df
    except Exception as e:
        logging.error(f"Error calculating price spread: {e}")
        df['price_spread'] = np.nan
        return df

def 
