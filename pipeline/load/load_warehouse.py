from helper.db import get_warehouse_engine


def load_warehouse(df):

    engine = get_warehouse_engine()

    df.to_sql(
        "car_sales",
        engine,
        if_exists="replace",
        index=False
    )

    print("Warehouse loaded successfully")