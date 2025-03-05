import boto3
import datetime
import json
import os
from pathlib import Path

# AWS Configuration
AWS_REGION = "us-east-1"  
BUCKET_NAME = "kp-eks-release" #bucket-name
# FOLDER_PREFIXES = [""]  # List for dir with bucket eg:- "stage/kp-lambda-account-usage-service/"
RETENTION_DAYS = 300  # Number of Days the data is kept in the bucket


s3 = boto3.client("s3")


current_date = datetime.datetime.now(datetime.timezone.utc)

def check_old_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME) # Prefix=prefix

    if "Contents" in response:
            for obj in response["Contents"]:
                file_key = obj["Key"]
                filename = Path(os.path.basename(file_key))
                last_modified = obj["LastModified"]
                age_days = (current_date - last_modified).days

                # Delete if older than retention period
                if filename.suffix:
                    if age_days > RETENTION_DAYS:
                        print(f"checking \033[0;33m{filename}\033[0m \033[1;31m(Age: {age_days} days)\033[0m")
                        # s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
                    else:
                        print(f"Skipping {filename} (Age: {age_days} days)")
    else:
        print(f"No files found in {BUCKET_NAME}")

if __name__ == "__main__":
    check_old_files()