from django.contrib import admin
from .models import Perro

# Register your models here.
class PerroAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'dueño']

admin.site.register(Perro, PerroAdmin)
