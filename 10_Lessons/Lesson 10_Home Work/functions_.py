import json

from Classes import Candidate

def load_candidates():
    with open ("candidates.json", "r", encoding = "utf-8") as file:
        file_data = json.load(file)
    return file_data

def get_all(file_data):
    candidates_list = []
    for item in file_data:
        candidate = Candidate(item['pk'], item['name'], item['picture'], item['position'], item['skills'])
        candidates_list.append(candidate)
    return candidates_list

def get_by_pk(pk, candidates_list):
    for item in candidates_list:
        if item.pk == pk:
            return item

def get_by_skill(skill_name, candidates_list):
    candidates_by_skill = []
    for item in candidates_list:
        if skill_name.lower() in item.skills.lower():
            candidates_by_skill.append(item)
    return candidates_by_skill
