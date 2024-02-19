import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

year = datetime.datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", current_year=year)


@app.route("/Projects")
def projects():
    return render_template('projects.html', current_year=year)


@app.route("/Resume")
def resume():
    return render_template('resume.html', current_year=year)


if __name__ == '__main__':
    app.run()
    