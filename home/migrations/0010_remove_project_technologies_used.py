# Generated by Django 5.0.6 on 2024-08-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_category_rank_project_rank_skillcategory_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies_used',
        ),
    ]
