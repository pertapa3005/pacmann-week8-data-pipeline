import pandas as pd


def transform_to_warehouse(
    car_sales: pd.DataFrame,
    car_brand: pd.DataFrame,
    us_state: pd.DataFrame
) -> pd.DataFrame:

    print("Starting transformation...")

    # =====================================
    # DATA CLEANING
    # =====================================

    car_sales = car_sales.copy()
    car_brand = car_brand.copy()
    us_state = us_state.copy()

    # Brand
    car_sales["brand_car"] = (
        car_sales["brand_car"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    car_brand["brand_name"] = (
        car_brand["brand_name"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # State
    car_sales["state"] = (
        car_sales["state"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.strip()
    )

    us_state["code"] = (
        us_state["code"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.strip()
    )

    # =====================================
    # MAPPING BRAND
    # =====================================

    df = car_sales.merge(
        car_brand,
        left_on="brand_car",
        right_on="brand_name",
        how="left"
    )

    # =====================================
    # MAPPING STATE
    # =====================================

    df = df.merge(
        us_state,
        left_on="state",
        right_on="code",
        how="left"
    )

    # =====================================
    # DATA QUALITY CHECK
    # =====================================

    missing_brand = df["brand_car_id"].isna().sum()
    missing_state = df["id_state"].isna().sum()

    print(f"Missing brand mapping : {missing_brand}")
    print(f"Missing state mapping : {missing_state}")

    # =====================================
    # WAREHOUSE SCHEMA
    # =====================================

    warehouse_df = pd.DataFrame({
        "id_sales": df["id_sales"],
        "year": df["year"],
        "brand_car_id": df["brand_car_id"],
        "model": df["model"],
        "trim": df["trim"],
        "body": df["body"],
        "transmission": df["transmission"],
        "vin": df["vin"],
        "id_state": df["id_state"],
        "condition": df["condition"],
        "odometer": df["odometer"],
        "color": df["color"],
        "interior": df["interior"],
        "seller": df["seller"],
        "mmr": df["mmr"],
        "sellingprice": df["sellingprice"],
        "saledate": df["saledate"]
    })

    # =====================================
    # REMOVE DUPLICATE
    # =====================================

    warehouse_df = warehouse_df.drop_duplicates()

    print(f"Final warehouse rows : {len(warehouse_df)}")

    return warehouse_df