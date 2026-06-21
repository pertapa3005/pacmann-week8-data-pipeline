# check_missing_brand.py

from extract.extract_staging import extract_staging_tables

car_sales, car_brand, us_state = extract_staging_tables()

missing_brand = set(car_sales["brand_car"].unique()) - set(car_brand["brand_name"].unique())

print("Jumlah brand tidak ketemu:", len(missing_brand))
print(sorted(missing_brand))