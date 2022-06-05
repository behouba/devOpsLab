"""program entry main file."""
from datetime import datetime

from flask import Flask, render_template


import pytz


def get_ru_time():
    """Function to get the current moscow time in string format."""
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")

def create_app():
    """Create new instance of Flask app."""
    app = Flask(__name__)

    @app.route('/')
    def index():

        ru_time = get_ru_time()

        return render_template("index.html", time = ru_time)
    return app



if __name__ == '__main__':
    create_app().run()
