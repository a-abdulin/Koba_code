from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return __name__

app.run(host='127.0.0.2', port=8000)
