from helper.minio_helper import get_minio_client

client = get_minio_client()

bucket_name = "models"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

client.fput_object(
    bucket_name,
    "car_price_model.pkl",
    "car_price_model.pkl"
)

print("Model uploaded successfully")