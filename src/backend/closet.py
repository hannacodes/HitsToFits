import os
from google.cloud import storage

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='bucketKey.json'

storage_client = storage.Client()

# accessing a bucket
closet = storage.get_bucket('bucket')

# upload to bucket (closet)
def uploadToBucket(blobName, filePath, bucketName):
    try:
        bucket = storage_client.get_bucket(bucketName)
        blob = bucket.blob(blobName)
        blob.upload_from_file_name(filePath)
        return True
    except Exception as e:
        print(e)
        return False
    
