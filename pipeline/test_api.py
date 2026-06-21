from extract.extract_api import extract_state_api

df = extract_state_api()

print(df.head())
print(df.shape)