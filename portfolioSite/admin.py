from django.contrib import admin
from portfolioSite.models import *


@admin.register(Index)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Projects)
class AuthorAdmin(admin.ModelAdmin):
    pass


# Register your models here.
