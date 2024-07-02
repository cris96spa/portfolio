from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    technologies_used = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name