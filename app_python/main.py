"""program entry main file."""
from datetime import datetime

import pytz

from flask import Flask, render_template

app = Flask(__name__)




def get_ru_time():
    """Function to get the current moscow time in string format."""
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")


visits_file = "visits.txt"


open(visits_file, 'w+', encoding="utf-8")


@app.route('/')
def index():
    ru_time = get_ru_time()

    with open(visits_file, 'a+', encoding="utf-8") as file:
        file.write("/ visited at: " + ru_time + "\n")
        file.close()
    return render_template("index.html", time = ru_time)


@app.route('/visits')
def visits():
    with open(visits_file, 'r', encoding="utf-8") as file:
        data = file.readlines()
    return render_template("visits.html", visits_log = data)




app.run(debug=True)
