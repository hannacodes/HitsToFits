from __future__ import absolute_import
# from __future__ import print_function
import google
from google.cloud import vision
from googleapiclient.discovery import build
import os
import json

# authenticate google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='hit2fitKey.json'

image_uri = 'gs://hit2fit/blue.png'

client = vision.ImageAnnotatorClient()
image = vision.Image() # Py2+3 if hasattr(vision, 'Image') else vision.types.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

def getLabels():
    print('Labels (and confidence score):')
    print('=' * 30)
    for label in response.label_annotations:
        print(label.description, '(%.2f%%)' % (label.score*100.))

# getLabels()

def getDominantColor():
    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    
    print("\nProperties:")
    domColor = props.dominant_colors.colors[0]
    colorString = domColor.color
    # color = json.loads(colorString)
    # print(color["red"], color["green"], color["blue"])

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return [colorString.red, colorString.green, colorString.blue]


print(getDominantColor())