import pandas as pd
from helper.db import get_staging_engine


def extract_staging_tables():

    engine = get_staging_engine()

    car_sales = pd.read_sql(
        "SELECT * FROM car_sales",
        engine
    )

    car_brand = pd.read_sql(
        "SELECT * FROM car_brand",
        engine
    )

    us_state = pd.read_sql(
        "SELECT * FROM us_state",
        engine
    )

    return car_sales, car_brand, us_state