from flask import Flask, render_template

from datetime import datetime

import pytz

# Function to get the current moscow time in string format
def get_ru_time():
    return datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():

        ru_time = get_ru_time()

        print(ru_time)
        return render_template("index.html", time = ru_time)
    
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()