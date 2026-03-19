import validate, ingest, processing
import pandas as pd


def main():
    df = ingest.ingest_csv("./data/raw/marketData.csv")
    df = validate.clean_df(df)
    df = processing.daily_return(df)
    print(df)


if __name__ == "__main__":
    main()