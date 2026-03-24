import sqlite3
import pandas as pd
import sys
from . import  logging_config
from  .logging_config import main_logger
logger =  logging_config.setup_logger('database_logger', 'app/tests/logs/database.log')
import pathlib
temp = pathlib.Path(__file__).parent.parent.parent.resolve().as_posix()
sys.path.append(temp)
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


# Database functions
def create_new_table(df : pd.DataFrame, db_name=config['database']['path'], table_name=config['database']['table_name']):
    # Create a new table in the database and insert data from the DataFrame
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        logger.info(f"Data successfully added to {db_name} in table {table_name}")
        conn.close()
    except Exception as e:
        logger.error(f"Error adding data to database: {e}")
        main_logger.error(f"Error adding data to database: {e}")




def append_to_table(df : pd.DataFrame, db_name=config['database']['path'], table_name=config['database']['table_name']):
    # Append data from the DataFrame to an existing table in the database
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='append', index=False)
        logger.info(f"Data successfully appended to {db_name} in table {table_name}")
        conn.close()
    except Exception as e:
        logger.error(f"Error appending data to database: {e}")
        main_logger.error(f"Error appending data to database: {e}")
