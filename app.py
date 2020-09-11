import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'smells_good'
app.config["MONGO_URI"] = 'mongodb+srv://sam_mckenna:YnNPIkpu2VIdHiqT@cluster0.wptnw.mongodb.net/smells_good?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/recipes')
def recipes():
    return render_template("home.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)