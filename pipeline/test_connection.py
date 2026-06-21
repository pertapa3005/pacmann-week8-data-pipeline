import pandas as pd
from helper.db import get_source_engine

engine = get_source_engine()

df = pd.read_sql(
    "SELECT COUNT(*) as total FROM car_sales",
    engine
)

print(df)