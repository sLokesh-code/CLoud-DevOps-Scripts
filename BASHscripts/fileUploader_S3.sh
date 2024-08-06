#!/bin/bash

#upload files to aws S3
s3_file_uploader () {
    local file="$1"
    echo "Available buckets: "
    aws s3 ls

    read -p "Enter the bucket name or create new bucket (y/n): " bucket_choice
    if [[ "$bucket_choice" == "y" || "$bucket_choice" == "Y" ]]; then
        read -p "Enter new bucket name: " new_bucket
        aws s3 mb s3://"$new_bucket"
        echo "$file is uploading to $new_bucket..."
        aws s3 mv "$file" s3://"$new_bucket"
    else
        read -p "Enter existing bucket name: " bucket_name
        echo "$file is uploading to $bucket_name..."
        aws s3 mv "$file" s3://"$bucket_name"
    fi
}

for file in "$@"; do
    if [ -f "$file" ]; then
        s3_file_uploader "$file"
    else
        echo "Error: $file does not exist"
    fi
done