from __future__ import absolute_import
# from __future__ import print_function
import google
from google.cloud import vision
from googleapiclient.discovery import build
import os
from closet import listBlobs

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='hit2fitKey.json'
bucketName = "hit2fit"


# gets the dominant color of one blob
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

# gets the colors of all blobs in a bucket
def getBucketColors(bucketName):
    bucketNames = listBlobs(bucketName)
    
    retList = []
    for blobName in bucketNames:
        retList.append(getDominantColor(blobName))
    
    return retList

# returns true if this is a shirt
def isShirt(blobName):
    shirt = ["T-shirt", "Shirt", "Active shirt"]
    uri = 'gs://hit2fit/' + blobName

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri
    response = client.label_detection(image=image)

    for label in response.label_annotations:
        if label.description in shirt:
            return True
        
    return False

# gets the colors of identified shirts in the bucket
def getShirtColors(bucketName):
    bucketNames = listBlobs(bucketName)

    shirtColors = []
    for blobName in bucketNames:
        if isShirt(blobName):
            shirtColors.append(getDominantColor(blobName))

    return shirtColors

# is this a pant
def isPant(blobName):
    pant = ["Jeans", "Pants", "Active pants"]
    uri = 'gs://hit2fit/' + blobName

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri
    response = client.label_detection(image=image)

    for label in response.label_annotations:
        if label.description in pant:
            return True
        
    return False

# gets the colors of identified pants in the bucket
def getPantColors(bucketName):
    bucketNames = listBlobs(bucketName)

    pantColors = []
    for blobName in bucketNames:
        if isPant(blobName):
            pantColors.append(getDominantColor(blobName))

    return pantColors

# testing function
def getLabels(blobName):
    image_uri = 'gs://hit2fit/' + blobName

    client = vision.ImageAnnotatorClient()
    image = vision.Image() # Py2+3 if hasattr(vision, 'Image') else vision.types.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)

    print('Labels (and confidence score):')
    print('=' * 30)
    for label in response.label_annotations:
        print(label.description, '(%.2f%%)' % (label.score*100.))

# gets the filename of a certain color
def getBestMatch(color):
    bucketNames = listBlobs("hit2fit")

    for blobName in bucketNames:
        if getDominantColor(blobName) == color:
            return str(blobName)

    return None

# return the shirts
def getShirts(bucket_name):
    blobs = listBlobs(bucket_name)

    shirtList = []
    for blob in blobs:
        if isShirt(blob):
            shirtList.append(blob)

    return shirtList

# return the pants
def getPants(bucket_name):
    blobs = listBlobs(bucket_name)

    pantList = []
    for blob in blobs:
        if isPant(blob):
            pantList.append(blob)

    return pantList
