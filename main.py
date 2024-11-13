from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def get_time():
    return time.strftime('%H:%M:%S')


if __name__ == '__main__':
    app.run()