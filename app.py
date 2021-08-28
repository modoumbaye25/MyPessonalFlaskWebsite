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


if __name__ == '__main__':
    app.run(debug=True)
