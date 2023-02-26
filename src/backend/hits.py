import spotipy
import os
import math
import json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
# this class gets the data from the song
load_dotenv()
CID = os.getenv('CLIENTID')
CIS = os.getenv('CLIENTSECRET')

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=CIS)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def getAllData(track_uri):
    return sp.audio_features(track_uri)[0]

# this gets the mode of the song
def getMode(features):
    return features["mode"]

def convertLoudness(loud): 
    power = 10**(loud/20)
    return power

# this gets the loudness of a song :)
def getLoudness(features):
    # normalize loudness
    loud = features["loudness"]
    return convertLoudness(loud)

def getEnergy(features):
    return features["energy"]

def getValence(features):
    return features["valence"]

def getDanceability(features):
    return features["danceability"]

def getName(features):
    track = sp.track(features["id"])
    return track["name"]

def getArtist(features):
    track = sp.track(features["id"])
    return track["artists"][0]["name"]

if __name__ == '__main__':
    print("enter a song: ")
    track_uri = input()
    features = getAllData(track_uri)
    print(getMode(features))
    print(getLoudness(features))
    print(getEnergy(features))
    print(getValence(features))
    print(getName(features))
    print(getArtist(features))