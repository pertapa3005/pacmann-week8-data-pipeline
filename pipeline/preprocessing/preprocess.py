import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data(df):

    # pilih fitur numerik saja
    features = [
        "year",
        "brand_car_id",
        "id_state",
        "condition",
        "odometer",
        "mmr"
    ]

    target = "sellingprice"

    data = df[features + [target]].copy()

    # isi null
    data = data.fillna(0)

    X = data[features]

    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print(f"Train : {len(X_train)}")
    print(f"Test  : {len(X_test)}")

    return X_train, X_test, y_train, y_test