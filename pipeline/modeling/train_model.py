import joblib

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


def train_model(
    X_train,
    X_test,
    y_train,
    y_test
):

    model = DecisionTreeRegressor(
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    print(f"MAE : {mae}")

    joblib.dump(
        model,
        "car_price_model.pkl"
    )

    print(
        "Model saved : car_price_model.pkl"
    )

    return model