from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Category, Contact

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Contact)