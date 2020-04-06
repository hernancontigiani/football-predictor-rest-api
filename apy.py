#!/usr/bin/env python
"""Football Predictor Rest API

Receives a home and away team in JSON format and return match prediction result
Example

127.0.0.1:port/predict?home_team=Argentina&away_team=Uruguay
result:win
"""

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from footballpredictor import FootballPredictor
import traceback

__author__ = "Hernan Contigiani"
__email__ = "hernan4790@gmail.com"
__version__ = "1.0.0"

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict') # Your API endpoint URL would consist /predict
def predict():
    if model.is_active == True:
        try:
            home_team = request.args.get('home_team')
            away_team = request.args.get('away_team')

            if home_team == None or away_team == None:
                return('Error parameters, please use 127.0.0.1:port/predict?home_team=Country1&away_team=Country2')

            prediction = model.predict(home_team=home_team ,away_team=away_team)
            result = "<h2>" + home_team + " vs " + away_team + "</h2>"
            result += home_team + ":" + prediction
            return(result)
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        return ('Model not loaded!')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line argument
    except:
        port = 5000 # If you don't provide any port then the port will be set to 12345
    
    model_path='football_predictor_model.pkl'
    db_path='football.db'
    model = FootballPredictor(model_path=model_path, db_path=db_path)
    if model.is_active == False:
        print("Error: Model file o database file not exits")
        print("Model path:", model_path)
        print("Database path:", db_path)
        
    app.run(port=port, debug=True)