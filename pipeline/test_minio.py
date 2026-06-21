from minio import Minio

client = Minio(
    "localhost:9001",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False
)

buckets = client.list_buckets()

for bucket in buckets:
    print(bucket.name)

print("MinIO connection success")