import os
import boto3
from app.config import settings

def upload_file(local_path: str, key: str):
    if settings.S3_BUCKET == "":
        dest_dir = "/tmp/agrisure_storage"
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, os.path.basename(local_path))
        with open(local_path, "rb") as fr, open(dest, "wb") as fw:
            fw.write(fr.read())
        return dest

    s3 = boto3.client("s3", region_name=settings.AWS_REGION)
    s3.upload_file(local_path, settings.S3_BUCKET, key)
    return f"s3://{settings.S3_BUCKET}/{key}"
