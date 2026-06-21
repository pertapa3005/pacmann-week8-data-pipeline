import pandas as pd
from helper.db import get_warehouse_engine


def extract_warehouse_data():

    engine = get_warehouse_engine()

    df = pd.read_sql(
        "SELECT * FROM car_sales",
        engine
    )

    print(f"Warehouse Rows : {len(df)}")

    return df