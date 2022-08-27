import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    is_blocked = random.choice([True, False])
    return render_template('hello.html', is_blocked=is_blocked)


app.run(host='127.0.0.3', port=5000)
