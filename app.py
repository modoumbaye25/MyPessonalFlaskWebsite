import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", current_year=year)


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/games")
def games():
    return render_template('games.html')


@app.route("/About")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
