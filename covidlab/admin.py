from django.contrib import admin
from .models import *
from datetime import datetime

class AnalisAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nranalis",)}

admin.site.register(Analis,AnalisAdmin)
