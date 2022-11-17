from django.db import models


class Contact(models.Model):
    my_name = models.CharField(max_length=30)
    phone = models.SmallIntegerField(default=123456789)
    email = models.EmailField(default="email@email.com")
    github = models.URLField(default="www.a.cz")
    linkedin = models.URLField(default="www.a.cz")


    def __str__(self):
        return self.my_name


class Projects(models.Model):
    type = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    url = models.URLField()


    def __str__(self):
        return self.name