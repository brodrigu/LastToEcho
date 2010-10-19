import lastfm
from pyechonest import config
from pyechonest import artist
from pyechonest import song
import pprint

last_fm_api_key = 'be0bd3798ac42fab39d4da707350bdd6'
echo_api_key = 'XXQUZTRTJZWLMLINE'

def get_echo_audio_url(artist_name, song_name):
    this_artist = artist.Artist(artist_name)
    audios = this_artist.get_audio(50,0)
    
    for audio in audios:
        if hasattr(audio, 'title') and audio.title.lower() ==song_name.lower():
            return audio.url
    return 0


last_fm_api = lastfm.Api(last_fm_api_key)
last_fm_user = last_fm_api.get_user('netbrad')
loved_tracks = last_fm_user.loved_tracks

config.ECHO_NEST_API_KEY = echo_api_key

for track in loved_tracks[:20]:
    url = get_echo_audio_url(track.artist.name, track.name)
    if url:
        print "%s: %s" % (track.name, url)
    else:
        print "%s: no url found" % (track.name)


    