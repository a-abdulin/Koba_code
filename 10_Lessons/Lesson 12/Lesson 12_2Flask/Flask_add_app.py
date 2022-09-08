from flask import Flask, request, render_template

app = Flask(__name__)
task_list = []

def print_tasks(task_list):
    print_list = ''
    for item in task_list:
        print_list += '<br>' + item
    return print_list

@app.route('/')
def main_page():
    return render_template('form_post.html')


@app.post('/add')
def add_page():
    task_list.append(request.values.get('text_name'))
    return f'Список задач: {print_tasks(task_list)}'


app.run()
