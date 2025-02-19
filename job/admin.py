from django.contrib import admin

# Register your models here.
from .models import Job


admin.site.register(Job)  # add job table to admin panel
