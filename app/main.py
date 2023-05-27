import os
from flask import Flask, jsonify, request
from app.utils import get_song_names, parse_data
from app.recommender import Model

app = Flask(__name__)

rec = Model()
rec.loadData()
rec.prepareModel()

@app.route('/')
def index():
  return 'The best recommended playlists from Pozytywka!'

@app.route('/playlist_ids', methods=['POST']) 
def playlist_ids():
    data = request.json
    user_ids = parse_data(data)
    song_ids = rec.createPlaylist(user_ids)
    return jsonify(users=user_ids, songs=song_ids)
    
@app.route('/playlist_names', methods=['POST']) 
def playlist_names():
    data = request.json
    user_ids = parse_data(data)
    song_ids = rec.createPlaylist(user_ids)
    songs = get_song_names(song_ids)
    return jsonify(users=user_ids, songs=songs)
  
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
