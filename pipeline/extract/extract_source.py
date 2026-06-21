import pandas as pd
from helper.db import get_source_engine


def extract_source_data():
    engine = get_source_engine()

    query = """
    SELECT *
    FROM car_sales
    """

    df = pd.read_sql(query, engine)

    print(f"Source Rows : {len(df)}")

    return df