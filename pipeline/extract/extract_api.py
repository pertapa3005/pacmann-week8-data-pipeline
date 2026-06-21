import pandas as pd
import requests


def extract_state_api():
    url = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/us_states_data/refs/heads/main/us_states.json"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["regions"])

    print(f"State Rows : {len(df)}")

    return df