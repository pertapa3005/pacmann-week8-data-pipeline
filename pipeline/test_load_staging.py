from extract.extract_source import extract_source_data
from extract.extract_api import extract_state_api
from extract.extract_sheet import extract_brand_sheet

from load.load_staging import (
    load_car_sales_staging,
    load_brand_staging,
    load_state_staging
)

car_df = extract_source_data()
state_df = extract_state_api()
brand_df = extract_brand_sheet()

load_car_sales_staging(car_df)
load_state_staging(state_df)
load_brand_staging(brand_df)