from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_data_from_json():
    data = request.json

    for item in data:
        with open("./assets/data.txt", "a", encoding="utf-8") as file:
            file.write(item.get("name") + "\n")
            file.write(item.get("phone") + "\n")
            file.write(item.get("email") + "\n")

    return jsonify({"result": "Данные записаны"})

app.run()