import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def extract_brand_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials/google_sheet.json",
        scope
    )

    client = gspread.authorize(creds)

    sheet = client.open_by_key(
        "1nQi-YDX9KRs5mmqT-iAC67nz4QyKLUyLOUpQatY5wOI"
    ).sheet1

    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    print(f"Brand Rows : {len(df)}")

    return df