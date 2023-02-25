import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
# this class gets the data from the song
load_dotenv()
CID = os.getenv('CLIENTID')
CIS = os.getenv('CLIENTSECRET')


#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=CIS)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

print("enter a song: ")
track_uri = input()


def getAllData():
    print(sp.audio_features(track_uri)[0])

getAllData()