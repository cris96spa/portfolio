from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    img = models.CharField(max_length=200)
    skills = models.ManyToManyField('Skill')
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    def __str__(self):
        return self.name
    