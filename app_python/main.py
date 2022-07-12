"""program entry main file."""
from datetime import datetime

import pytz

from flask import Flask, render_template





def get_ru_time():
    """Function to get the current moscow time in string format."""
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")


def create_app():
    "Initialize the app"
    app = Flask(__name__)

    visits_log = "visits.txt"


    open(visits_log, 'w+', encoding="utf-8")

    @app.route('/')
    def index():
        "Website home page handler"
        ru_time = get_ru_time()

        with open(visits_log, 'a+', encoding="utf-8") as file:
            file.write("/ visited at: " + ru_time + "\n")
            file.close()
        return render_template("index.html", time = ru_time)


    @app.route('/visits')
    def visits():
        "Website visits log output page handler"
        with open(visits_log, 'r', encoding="utf-8") as file:
            data = file.readlines()
        return render_template("visits.html", visits_log = data)

    return app

if __name__ == '__main__':
    create_app().run()