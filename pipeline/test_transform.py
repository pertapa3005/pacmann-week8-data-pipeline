from extract.extract_staging import (
    extract_staging_tables
)

from transform.transform import (
    transform_to_warehouse
)

car_sales, car_brand, us_state = (
    extract_staging_tables()
)

warehouse_df = transform_to_warehouse(
    car_sales,
    car_brand,
    us_state
)

print(warehouse_df.head())

print(warehouse_df.shape)

print(
    warehouse_df[
        ["brand_car_id", "id_state"]
    ].isnull().sum()
)