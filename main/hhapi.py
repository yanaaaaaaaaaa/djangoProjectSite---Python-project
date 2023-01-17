from datetime import datetime

import requests


class HhVacancy:
    def __init__(self, name, description, skills, employer_name, area_name, published_at, salary_from, salary_to,
                 salary_currency):
        self.name = name
        self.description = description
        self.skills = skills
        self.employer_name = employer_name
        self.area_name = area_name
        self.published_at = published_at
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency

        if salary_to is not None and salary_from is not None:
            self.html_salary = f'{salary_from} - {salary_to} {salary_currency}'
        elif salary_from is not None:
            self.html_salary = f'от {salary_from} {salary_currency}'
        elif salary_to is not None:
            self.html_salary = f'до {salary_to} {salary_currency}'
        else:
            self.html_salary = 'зп не указана'

        if len(skills) > 0:
            self.html_skills = ', '.join(self.skills)
        else:
            self.html_skills = 'не указано'

        self.html_date = published_at.strftime('%d.%m.%Y %H:%M:%S')


def get_vacancies(search, count):
    response = requests.get('https://api.hh.ru/vacancies', {
        'text': search,
        'per_page': count,
        'page': 1,
        'order_by': 'publication_time',
        'date_from': '2022-12-26T00:00+0300',
        'date_to': '2022-12-27T00:00+0300',
    })
    print(response.text)

    result = []
    for el in response.json()['items']:
        hh_id = el['id']
        name = el['name']
        full_el = requests.get(f'https://api.hh.ru/vacancies/{hh_id}')
        full_el_json = full_el.json()
        description = full_el_json['description']
        skills = []
        for skill_arg in full_el_json['key_skills']:
            skills.append(skill_arg['name'])
        employer_name = el['employer']['name']
        area_name = el['area']['name']
        published_at = datetime.strptime(el['published_at'], "%Y-%m-%dT%H:%M:%S%z")
        s_from, s_to, s_currency = None, None, None
        if el['salary'] is not None:
            s_from = el['salary']['from']
            s_to = el['salary']['to']
            s_currency = el['salary']['currency']
        result.append(HhVacancy(
            name=name,
            description=description,
            skills=skills,
            employer_name=employer_name,
            area_name=area_name,
            published_at=published_at,
            salary_from=s_from,
            salary_to=s_to,
            salary_currency=s_currency
        ))
    return result
