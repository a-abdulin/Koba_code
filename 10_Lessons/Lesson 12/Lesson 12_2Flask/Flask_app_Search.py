from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('form.html')

@app.get('/search')
def search_page():
    s = request.args.get('s')
    return f'Вы ввели слово {s}'

app.run()
