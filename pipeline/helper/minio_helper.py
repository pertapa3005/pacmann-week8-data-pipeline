from minio import Minio


def get_minio_client():

    client = Minio(
        "localhost:9001",
        access_key="minioadmin",
        secret_key="minioadmin123",
        secure=False
    )

    return client