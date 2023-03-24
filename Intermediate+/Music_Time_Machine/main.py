# Day 46 - Musical Time Machine
'''Creates a spotify playlist of the top 100 songs from a specified date.'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import requests
from bs4 import BeautifulSoup

date = input('Which year do you want to travel to?\
 Type the date in this format YYYY-MM-DD:')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.o-chart-results-list__item h3.c-title')
song_titles = [song.getText().strip() for song in titles]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://localhost:8888/callback',
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path='token.txt'
    )
)

user_id = sp.current_user()['id']

song_uris = []
year = date.split('-')[0]
for song in song_titles:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f'{date} Billboard 100',
    public=False)

sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=song_uris
)
