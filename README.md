# football-predictor-rest-api

Python Rest API based on Flask for football match result prediction

In this repository you will find these important files:
* apy.py --> Script of our REST API server based on Flask
* footballpredictor --> football predictor model class
* football_predictor_model.pkl --> Our model trained based on this notebook:
	* https://github.com/hernancontigiani/football-result-predictor
* football.db --> Database creadted based on notebook:
	* https://github.com/hernancontigiani/football-result-predictor

Usage:
First run the Rest API Flask server
`python ./api.py`

Then open your browser and enter this URL example:
127.0.0.1:port/predict?home_team=Argentina&away_team=Uruguay

You will get something like this:
![ANFIS training](/images/test.png)

Where "home_team" is the local country team
Where "away_team" is the away country team

This API return the result based on classifier model trained with that from 1872 to present

Future features:
- Possibility to add new result to database.
- Train model from current database.
- Get statistical results about one team.
- Get statistical results about two teams.
