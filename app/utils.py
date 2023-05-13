SONGS_TOTAL=20

def get_songs(users):
    songs = ["song1", "song2"]
    return songs, users

def parse_data(data):
    try:
        users = data["users"]
        count = data.get("count", SONGS_TOTAL)
        if not isinstance(users, list):
            raise Exception("Incorrect parameters, a list of users should be provided.")
        return users, count
    except KeyError as e:
        msg = "Invalid request, field \"users\" is missing."
        #TODO: better error handling/displaying
        print(msg)
