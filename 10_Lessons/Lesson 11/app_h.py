from flask import render_template, Flask

app = Flask(__name__)

# with app.app_context():
page = render_template("index.html", name="Andrey")

print(page)
