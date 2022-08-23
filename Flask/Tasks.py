from flask import Flask

app = Flask(__name__)

letters = { 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", }

@app.route('/get_letter/<int:index>')
def page_letter(index):
    letter = letters.get(index)
    return letter

app.run()
