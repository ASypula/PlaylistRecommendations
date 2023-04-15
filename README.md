# IUM

Program for generating playlist recommendations.

### Preliminary API calls and Flask server runs
Steps:
1. Install Flask: ```pip install Flask```
2. Run the server on localhost: ```python3 app/main.py```

Testing:
* Use curl for making test POST requests
* Template for json content:
```
{
    "count": n,
    "users": [
        x, y, z
    ]
}
```
count - required number of songs in the playlist, field is not mandatory, if missing will be set to default value = 20

users - a list of users' ids
* Example curl: 
```
# On Linux
curl -i -X POST -H "Content-Type: application/json" -d "{"count": 5, "users": [1, 3, 4]}" http://127.0.0.1:5000/playlist
# On Windows
curl -i -X POST -H "Content-Type: application/json" -d "{\"count\": 5, \"users\": [1, 3, 4]}" http://127.0.0.1:5000/playlist
```
<!-- On Windows the escape \" in keys is required in the curl command -->

* By default the server should expose the port 5000
* In return the response should include random strings as songs and the received ids of users