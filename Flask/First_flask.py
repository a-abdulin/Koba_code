from flask import Flask

app = Flask(__name__)

@app.route("/", view_func=page_test)

def page_test():
    return "Ваше первое приложение"

