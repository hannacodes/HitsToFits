import os
from google.cloud import storage

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='bucketKey.json'
storage_client = storage.Client()
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"
    
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    # Note: The call returns a response only when the iterator is consumed.
    blobList = []
    for blob in blobs:
        blobList.append(blob.name)
    
    return blobList

# # accessing a bucket
# closet = storage.get_bucket('bucket')

# upload to bucket
# def uploadToBucket(fileName):
