from flask import Flask, jsonify, request
from utils import get_songs, parse_data

app = Flask(__name__)

@app.route('/')
def index():
  return 'The best recommended playlists from Pozytywka!'

    
@app.route('/playlist', methods=['POST']) 
def playlists():
    data = request.json
    users1, count = parse_data(data)
    songs1, users2 = get_songs(users1)
    return jsonify(users=users2, songs=songs1)
  
if __name__=='__main__':
    app.run(debug=True)
