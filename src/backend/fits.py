from __future__ import absolute_import
# from __future__ import print_function
import google
from google.cloud import vision
from googleapiclient.discovery import build
import os
from closet import list_blobs

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='hit2fitKey.json'


def getDominantColor(blobName):
    image_uri = 'gs://hit2fit/' + blobName

    client = vision.ImageAnnotatorClient()
    image = vision.Image() # Py2+3 if hasattr(vision, 'Image') else vision.types.Image()
    image.source.image_uri = image_uri

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    
    domColor = props.dominant_colors.colors[0]
    colorString = domColor.color

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return [int(colorString.red), int(colorString.green), int(colorString.blue)]

def getBucketColors(bucketName):
    bucketNames = list_blobs(bucketName)
    
    retList = []
    for blobName in bucketNames:
        retList.append(getDominantColor(blobName))
    
    return retList
