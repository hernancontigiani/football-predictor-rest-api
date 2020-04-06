"""Football Predictor Classifier Model

This class is the interface yo the classifier ML model and database

"""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble  import AdaBoostClassifier
from sklearn.externals import joblib
import sqlite3

__author__ = "Hernan Contigiani"
__email__ = "hernan4790@gmail.com"
__version__ = "1.0.0"

class FootballPredictor:
    """Football predictor model class"""

    def __init__(self,model_path, db_path):
        
        if os.path.isfile(model_path) == False or os.path.isfile(db_path) == False:
            self.is_active = False
            return

        self.model = joblib.load(model_path)
        self.db_path = db_path
        self.is_active = True

    def predict (self,home_team, away_team):

        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        home_team_formated = home_team.title()
        c.execute('SELECT id FROM teams WHERE country =(?)', (home_team_formated,))
        query_output = c.fetchone()

        if query_output == None:
            return "Invalid home_team country"
        home_team = query_output[0]

        away_team_formated = away_team.title()
        c.execute('SELECT id FROM teams WHERE country =(?)', (away_team_formated,))
        query_output = c.fetchone()

        if query_output == None:
            return "Invalid away_team country"
        away_team = query_output[0]

        X_test = [[home_team,away_team]]
        yhat = self.model.predict(X_test)
        print(yhat[0])
        return yhat[0]


