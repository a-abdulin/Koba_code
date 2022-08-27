from flask import Flask, render_template
from candidates import Candidates
from utils import get_all, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

candidate_list = get_all()

@app.route("/")
def page_index():
    return render_template('list.html', items=candidate_list)

@app.route("/candidate/<id>")
def page_candidate_by_id(id):
    candidate=get_candidate_by_id(candidate_list, id)
    return render_template('single.html', item=candidate)

@app.route("/search/<candidate_name>")
def page_candidate_by_name(candidate_name):
    candidates=get_candidates_by_name(candidate_list, candidate_name)
    return render_template('search.html', count=len(candidates), items=candidates)

@app.route("/skill/<skill_name>")
def page_candidate_by_skill(skill_name):
    candidates=get_candidates_by_skill(candidate_list, skill_name)
    return render_template('skill.html', skill_name=skill_name, count=len(candidates), items=candidates)


app.run(host='127.0.0.1', port=5000)
