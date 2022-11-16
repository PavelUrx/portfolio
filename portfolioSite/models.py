from django.db import models


class Index(models.Model):
    my_name = models.CharField(max_length=30)

class Projects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    url = models.URLField()