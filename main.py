import os
from flask import Flask, render_template, json, current_app as app
from flask_pymongo import PyMongo
import import_csv

app = Flask(__name__)

data_list = {}
app.config["MONGO_URI"] = "mongodb://localhost:27017/project_1"
mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/data")
def data():
    filename = 'data/2015.json'
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
        for x in data:
            rank = x['rank']
            country = x['country']
            score = x['score']
            gdp = x['gdp']
            social_support = x['social_support']
            life_expectancy = x['life_expectancy']
            freedom = x['freedom']
            generosity = x['generosity']
            corruption = x['corruption']
            #data_list.append([rank, country, score, gdp, social_support, life_expectancy, freedom, generosity, corruption])
        
        data_list = {
            'rank': rank,
            'country': country,
            'score': score,
            'GDP': gdp,
            'social_support': social_support,
            'life_expectency': life_expectancy,
            'freedom': freedom,
            'generosity': generosity,
            'corruption': corruption
        }
    

    return render_template("home.html", data = data_list)


if __name__ == "__main__":
    app.run(debug=True)