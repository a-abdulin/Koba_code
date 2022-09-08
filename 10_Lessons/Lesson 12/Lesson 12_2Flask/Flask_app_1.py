from flask import Flask, request

app = Flask(__name__)


@app.get('/search')
def search_page():
    s = request.args['s']
    add_arg = request.args['p']
    return f'Вы ввели слово {s} {add_arg}'


app.run(port=5000)
