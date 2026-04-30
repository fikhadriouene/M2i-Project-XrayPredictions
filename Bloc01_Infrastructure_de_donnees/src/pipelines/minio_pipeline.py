from storage.minio_client import *
import os
from config.settings import (
MINIO_RAW_BUCKET_IMAGES,
MINIO_RAW_BUCKET_METADATA,
PATH_RAW_DATASET_IMAGES,
PATH_RAW_DATASET_METADATA
)


mc = MinIOClient()

def raw_ingestion(mc: MinIOClient):
    if not mc.bucket_exists(MINIO_RAW_BUCKET_IMAGES):
        mc.create_bucket(MINIO_RAW_BUCKET_IMAGES)

    if not mc.bucket_exists(MINIO_RAW_BUCKET_METADATA):
        mc.create_bucket(MINIO_RAW_BUCKET_METADATA)

    for file_name in os.listdir(PATH_RAW_DATASET_IMAGES):
        file_path = os.path.join(PATH_RAW_DATASET_IMAGES, file_name)

        if os.path.isfile(file_path):
            mc.upload_file(
                bucket_name=MINIO_RAW_BUCKET_IMAGES,
                object_name=file_name,
                file_path=file_path
            )

    for file_name in os.listdir(PATH_RAW_DATASET_METADATA):
        file_path = os.path.join(PATH_RAW_DATASET_METADATA, file_name)

        if os.path.isfile(file_path):
            mc.upload_file(
                bucket_name=MINIO_RAW_BUCKET_METADATA,
                object_name=file_name,
                file_path=file_path
            )