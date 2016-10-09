from django.contrib import admin
from related_admin import RelatedFieldAdmin
from .models import *

class AdminFecha(admin.ModelAdmin):
    search_fields = ['fecha']
    date_hierarchy = 'fecha'

class AdminEntrada(admin.TabularInline):
    model = Entrada

class AdminVacuna(admin.TabularInline):
    model = Vacuna

class AdminAnimal(RelatedFieldAdmin):
    search_fields = ['nombre', 'dueño', 'telefono']
    list_display = ('especie__nombre', 'especie__imagen')
    inlines = [
        AdminEntrada, AdminVacuna
    ]

admin.site.register(Animal, AdminAnimal)

admin.site.register(MetaVacuna)
admin.site.register(Raza)
admin.site.register(Especie)
