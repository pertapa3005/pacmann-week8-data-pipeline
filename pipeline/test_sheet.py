# test_sheet.py

from extract.extract_sheet import extract_brand_sheet

df = extract_brand_sheet()

print(df.head())
print(df.shape)