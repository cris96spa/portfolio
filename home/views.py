from django.shortcuts import render
from home import models
# Create your views here.

def home(request):
    return render(request, 'home.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')