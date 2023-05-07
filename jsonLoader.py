import json

def readJSONL(fileName):
    data = []
    with open(fileName) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def getArtists():
    return readJSONL('./IUM_Zad_03_01_v4/artists.jsonl')


def getSessions():
    return readJSONL('./IUM_Zad_03_01_v4/sessions.jsonl')

def getTracks():
    return readJSONL('./IUM_Zad_03_01_v4/tracks.jsonl')

def getUsers():
    return readJSONL('./IUM_Zad_03_01_v4/users.jsonl')
