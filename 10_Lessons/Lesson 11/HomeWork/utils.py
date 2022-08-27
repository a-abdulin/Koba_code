import json

from candidates import Candidates


def load_file_(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    data_file = load_file_("candidates.json")
    candidate_list = []
    for item in data_file:
        candidate = Candidates(item["id"], item['name'], item['picture'], item['position'], item['gender'], item['age'],
                               item['skills'])
        candidate_list.append(candidate)
    return candidate_list


def get_candidate_by_id(data, candidate_id):
    for item in data:
        if item.id == int(candidate_id):
            return (item)
    return (None)


def get_candidates_by_name(data, candidate_name):
    candidates_with_name = []
    for item in data:
        if candidate_name.lower() in item.name.lower():
            candidates_with_name.append(item)
    return (candidates_with_name)


def get_candidates_by_skill(data, skill_name):
    candidates_with_skills = []
    for item in data:
        if skill_name.lower() in item.skills.lower():
            candidates_with_skills.append(item)
    return (candidates_with_skills)
