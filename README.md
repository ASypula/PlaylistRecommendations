# IUM

Program for generating playlist recommendations.
Can be run either using Docker container or Flask with Python3

## Local setup
1. Place folder with data - "IUM_Zad_03_01_v4" at the same level as other folders e.g. app
2. Run the main file: ``` python3 app/main.py ```

## Docker setup
1. Build the docker image
```docker image build -t ium_pozytywka . ```
2. Run a new container
```docker run -p 5000:5000 -d ium_pozytywka ```
3. Test with example curl shown at the bottom. As the port-binding was used, the application will be visible also under localhost:5000

## Flask server on localhost
Steps:
1. Install Flask: ```pip install Flask```
2. Run the server on localhost: ```python3 app/main.py```

## Usage
* Use curl for making test POST requests
* Template for json content:
```
{
    "user_ids": [
        x, y, z
    ]
}
```
users - a list of users' ids
* Example curl: 
```
# On Linux
curl -i -X POST -H "Content-Type: application/json" -d "{"users": [101, 103, 104]}" http://127.0.0.1:5000/playlist_names
# On Windows
curl -i -X POST -H "Content-Type: application/json" -d "{\"users\": [101, 103, 104]}" http://127.0.0.1:5000/playlist_names
```
<!-- On Windows the escape \" in keys is required in the curl command -->

* By default the server should expose the port 5000
* In return the response should include names of the songs chosen for the playlist and the received ids of users

## Experiment A/B
Running experiment A/B for two models: the custom one implemented in the application
and a random one that generates a list of track ids of required length.
Experiment can be run either with default parameters: 20 iterations for each number of users
given for the playlist creation. Numbers of users by default are 3, 6, 9.
```
python3 experiment/experiment_AB.py
```
Example for custom parameters
```
python3 experiment/experiment_AB.py 3 2 3 4
```
First parameter is the number of iterations and the rest are the counts of users for which tests are supposed to be run.

Experiment results will be saved to an output file test_results.txt
In the meantime all steps of the experiment with current state and results will be logged with the set importance to "info".

## Tests
Automated tests are created both for the utility functions as well as the main functionality of the model.
Commands for running the tests:
```
python3 tests/test_models.py
python3 tests/test_util_funcs.py
```