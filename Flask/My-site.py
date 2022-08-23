from flask import Flask

app = Flask(__name__)
@app.route("/")
def page_index():
    return "Стартовая страница"

@app.route("/profile/<int:usid>")
def page_profile(usid):
    print(usid)
    print(type(usid))
    return f"<h1>Профиль пользователя: {usid}<h1>"

@app.route("/feed/")
def page_feeds():
    print ('Какой-то текст!')
    return f"<h1>Лента пользователя<h1>"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route('/catalog/items/<itemid>')
def profile(itemid):
    print (itemid)
    return f'<h1>Страничка товара {itemid}</h1>'

app.run (host='127.0.0.2', port=5000)
