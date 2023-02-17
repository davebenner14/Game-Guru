from django.contrib import admin

# Register your models here.
from .models import Vid, Progress

# Register your models here
admin.site.register(Vid)
admin.site.register(Progress)
