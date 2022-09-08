from flask import Flask, request

app = Flask(__name__)


@app.get('/search')
def search_page():
    try:
        s = request.args.get('s')
        if s is None:
            raise TypeError
    except TypeError:
        return f'Вы ничего не ввели'
    else:
        return f'Вы ввели слово {s}'


app.run()
