from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.get('/books')
def read_books():
    return jsonify({"content": "Получаем все книжки"})


@app.route('/books/‹int:book_id›/', methods=['GET'])
def read_book(book_id):
    return jsonify({"content": f"Получаем книжку {book_id}"})


# @app.route('/books/‹book_id›/', methods=['PUT'])
# def update_book(book_id):
#     return jsonify({"content": f"Обновляем книжку {book_id}"})
#
#
# @app.route('/books/‹book_id›/', methods=['DELETE'])
# def delete_book(book_id):
#     return jsonify({"content": f"Удаляем книжку {book_id}"})


app.run()
