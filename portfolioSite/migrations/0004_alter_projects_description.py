# Generated by Django 4.1.3 on 2022-11-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioSite', '0003_projects_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
