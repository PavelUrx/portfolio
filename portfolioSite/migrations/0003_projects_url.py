# Generated by Django 4.1.3 on 2022-11-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioSite', '0002_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='url',
            field=models.URLField(default='#'),
            preserve_default=False,
        ),
    ]
