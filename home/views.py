from django.shortcuts import render
from home import models
# Create your views here.

def home(request):
    projects = models.Project.objects.order_by('rank', 'name')
    categories = models.Category.objects.order_by('name')
    skill_categories = models.SkillCategory.objects.order_by('name')
    skills = models.Skill.objects.order_by('-level', )
    return render(request, 'home.html', {'projects': projects, 'categories': categories, 'skill_categories': skill_categories, 'skills': skills})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')
