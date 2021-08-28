import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    year = datetime.datetime.now().year
    return render_template("index.html", current_year=year)


@app.route("/projects")
def projects():
    random_number = random.randint(1, 10)
    return render_template('projects.html', num=random_number)

@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/About")
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)
