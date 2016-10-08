from django.contrib import admin
from related_admin import RelatedFieldAdmin
from .models import *

# Register your models here.
class AdminAnimal(RelatedFieldAdmin):
    search_fields = ['nombre', 'dueño', 'telefono']
    list_display = ('especie__nombre', 'especie__imagen')

class AdminEntrada(admin.ModelAdmin):
    search_fields = ['fecha']
    date_hierarchy = 'fecha'

admin.site.register(Animal, AdminAnimal)
admin.site.register(Entrada, AdminEntrada)
admin.site.register(Vacuna, AdminEntrada)

admin.site.register(Raza)
admin.site.register(Especie)
