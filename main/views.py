from django.shortcuts import render

from main.hhapi import get_vacancies
from main.models import *


def main(request):
    obj = HomePage.objects.first()
    return render(request, 'main/main.html', {'obj': obj})


def demand(request):
    obj = DemandPage.objects.first()
    return render(request, 'main/demand.html', {'obj': obj})


def geography(request):
    obj = GeographyPage.objects.first()
    return render(request, 'main/geography.html', {'obj': obj})


def skills(request):
    objects = SkillYear.objects.order_by('year').all()
    test_obj = objects[0]
    return render(request, 'main/skills.html', {'objects': objects, 'test_obj': test_obj})


def last_vacancies(request):
    obj = VacancyPage.objects.first()
    vacs = get_vacancies(obj.search, obj.count)
    return render(request, 'main/last_vacancies.html', {'last_vacancies': vacs})
