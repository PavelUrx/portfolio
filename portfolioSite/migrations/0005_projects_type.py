# Generated by Django 4.1.3 on 2022-11-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioSite', '0004_alter_projects_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='type',
            field=models.CharField(default='pwf', max_length=3),
            preserve_default=False,
        ),
    ]