import os
from flask import Flask, jsonify, request
from utils import get_song_names, parse_data
from recommender import get_playlist

app = Flask(__name__)

@app.route('/')
def index():
  return 'The best recommended playlists from Pozytywka!'

    
@app.route('/playlist', methods=['POST']) 
def playlists():
    data = request.json
    users, count = parse_data(data)
    song_ids = get_playlist(users)
    songs = get_song_names(song_ids)
    return jsonify(users=users, songs=songs)
  
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
