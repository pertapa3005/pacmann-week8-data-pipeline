from helper.db import get_staging_engine


def load_car_sales_staging(df):

    engine = get_staging_engine()

    df.to_sql(
        "car_sales",
        engine,
        if_exists="replace",
        index=False
    )

    print("car_sales loaded")


def load_brand_staging(df):

    engine = get_staging_engine()

    df.to_sql(
        "car_brand",
        engine,
        if_exists="replace",
        index=False
    )

    print("car_brand loaded")


def load_state_staging(df):

    engine = get_staging_engine()

    df.to_sql(
        "us_state",
        engine,
        if_exists="replace",
        index=False
    )

    print("us_state loaded")