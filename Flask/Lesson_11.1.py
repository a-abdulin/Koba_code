from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


app.run()