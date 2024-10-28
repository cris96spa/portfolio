from django.shortcuts import render
from home.models import (
    Project,
    Category,
    SkillCategory,
    Skill,
)
from django.http import (
    HttpRequest,
    HttpResponse,
)


def home(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.order_by('rank', 'name')
    categories = Category.objects.order_by('rank', 'name')
    skill_categories = SkillCategory.objects.order_by('rank', 'name')
    skills = Skill.objects.order_by(
        '-level',
    )
    return render(
        request,
        'home.html',
        {
            'projects': projects,
            'categories': categories,
            'skill_categories': skill_categories,
            'skills': skills,
        },
    )
