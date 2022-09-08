from flask import Flask, request, render_template

app = Flask(__name__)

# Создаем множество расширений
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# Максимальный объем контента
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/')
def main_page():
    return render_template('form_file.html')

@app.route("/upload", methods=["POST"])
def upload_page():
    file = request.files.get('picture')
    file_name = file.filename
    # Получаем расширение файла
    extension = file_name.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        file.save(f'./uploads/{file_name}')
        return f'Файл загружен!'
    else:
        return 'Не допустимое расширение файла!'

@app.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413

app.run()
