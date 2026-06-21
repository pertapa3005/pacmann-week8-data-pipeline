from extract.extract_staging import extract_staging_tables
from transform.transform import transform_to_warehouse
from load.load_warehouse import load_warehouse

car_sales, car_brand, us_state = extract_staging_tables()

warehouse_df = transform_to_warehouse(
    car_sales,
    car_brand,
    us_state
)

load_warehouse(warehouse_df)