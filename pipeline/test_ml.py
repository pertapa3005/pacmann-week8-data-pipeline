from extract.extract_warehouse import (
    extract_warehouse_data
)

from preprocessing.preprocess import (
    preprocess_data
)

from modeling.train_model import (
    train_model
)

df = extract_warehouse_data()

X_train, X_test, y_train, y_test = (
    preprocess_data(df)
)

train_model(
    X_train,
    X_test,
    y_train,
    y_test
)