from minio import Minio
from minio.error import S3Error
from config.settings import (
    MINIO_ENDPOINT,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY
)


class MinIOClient:

    def __init__(self):
        self.client = Minio(
            MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False
        )


    # Buckets
    def bucket_exists(self, bucket_name: str) -> bool:
        return self.client.bucket_exists(bucket_name)

    def create_bucket(self, bucket_name: str):
        if not self.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    # Upload
    def upload_file(
        self,
        bucket_name: str,
        object_name: str,
        file_path: str
    ):
        self.client.fput_object(
            bucket_name,
            object_name,
            file_path
        )

    # Download a file
    def download_file(
        self,
        bucket_name: str,
        object_name: str,
        file_path: str
    ):
        self.client.fget_object(
            bucket_name,
            object_name,
            file_path
        )

    # Get an object
    def get_object(self, bucket_name: str, object_name: str):
        return self.client.get_object(bucket_name, object_name)


    # List objects
    def list_objects(self, bucket_name: str, prefix: str = ""):
        return self.client.list_objects(bucket_name, prefix=prefix, recursive=True)


    # Delete
    def delete_object(self, bucket_name: str, object_name: str):
        self.client.remove_object(bucket_name, object_name)