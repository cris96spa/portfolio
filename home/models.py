from django.db.models import (
    Model,
    CharField,
    TextField,
    URLField,
    ForeignKey,
    ManyToManyField,
    IntegerField,
    AutoField,
    CASCADE,
)
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Category(Model):
    name: CharField = CharField(max_length=100)
    tag: CharField = CharField(max_length=100)
    rank: IntegerField = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.name


class Project(Model):
    id: AutoField = AutoField(primary_key=True)
    name: CharField = CharField(max_length=200)
    short_description: CharField = CharField(max_length=300)
    description: TextField = TextField()
    category: ForeignKey = ForeignKey(Category, on_delete=CASCADE)
    github_link: URLField = URLField(blank=True, null=True)
    demo_link: URLField = URLField(blank=True, null=True)
    img: CharField = CharField(max_length=200)
    skills: ManyToManyField = ManyToManyField('Skill')
    rank: IntegerField = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.name


class SkillCategory(Model):
    name: CharField = CharField(max_length=100)
    tag: CharField = CharField(max_length=100)
    rank: IntegerField = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.name


class Skill(Model):
    name: CharField = CharField(max_length=100)
    category: ForeignKey = ForeignKey(SkillCategory, on_delete=CASCADE)
    level: IntegerField = IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name
