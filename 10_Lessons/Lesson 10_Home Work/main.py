from functions_ import load_candidates, get_all, get_by_pk, get_by_skill
from flask import Flask
from Classes import Candidate

app = Flask(__name__)

file_data = load_candidates()
candidates_list = get_all(file_data)

@app.route("/")
def page_index():
    string = '<pre>'
    for item in candidates_list:
        string += f'Имя кандидата - {item.name} \n' \
                  f'Позиция кандидата - {item.position} \n' \
                  f'Навыки через запятую - {item.skills} \n \n'
    string += '</pre>'
    return string

@app.route("/candidates/<int:pk>")
def page_candidate(pk):
    candidate = get_by_pk(pk, candidates_list)
    string = f'<img src={candidate.picture}> </br>'
    string += '<pre>'
    string += f'Имя кандидата - {candidate.name} \n' \
              f'Позиция кандидата - {candidate.position} \n' \
              f'Навыки через запятую - {candidate.skills} \n'
    string += '</pre>'
    print(string)
    return string

@app.route("/skills/<skill>")
def page_skills(skill):
    candidates_by_skill = get_by_skill(skill, candidates_list)
    string = '<pre>'
    for item in candidates_by_skill:
        string += f'Имя кандидата - {item.name} \n' \
                  f'Позиция кандидата - {item.position} \n' \
                  f'Навыки через запятую - {item.skills} \n \n'
    string += '</pre>'
    return string

app.run (port=8000)
