from __future__ import absolute_import
# from __future__ import print_function
import google
from google.cloud import vision
from googleapiclient.discovery import build
import os

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='hit2fitKey.json'

image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'

client = vision.ImageAnnotatorClient()
image = vision.Image() # Py2+3 if hasattr(vision, 'Image') else vision.types.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))