from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def get_time():
    now_time = f'Сейчас: {time.strftime('%H:%M:%S')}'
    return now_time


if __name__ == '__main__':
    app.run()