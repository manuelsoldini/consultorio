from django.contrib import admin
from related_admin import RelatedFieldAdmin
from ajax_select.admin import AjaxSelectAdminTabularInline
from ajax_select.fields import autoselect_fields_check_can_add
from .models import *
from .forms import *

class AdminImg(admin.StackedInline):
    fields = ( 'image_tag', 'nombre')
    readonly_fields = ('image_tag',)


class AdminRaza(AdminImg):
    model = Raza


class AdminEspecie(AdminImg):
    model = Especie


class AdminFecha(admin.ModelAdmin):
    search_fields = ['fecha']
    date_hierarchy = 'fecha'


class AdminEntrada(admin.TabularInline):
    model = Entrada


class AdminVacuna(AjaxSelectAdminTabularInline):
    model = Vacuna
    form = VacunaInlineForm


class AdminAnimal(RelatedFieldAdmin):
    search_fields = ['nombre', 'dueño', 'telefono']
    list_display = ('especie__nombre', 'especie__imagen')
    inlines = [
        AdminEntrada, AdminVacuna, #AdminRaza, AdminEspecie,
    ]
    form = AnimalForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(AdminAnimal, self).get_form(request, obj, **kwargs)
        autoselect_fields_check_can_add(form, self.model, request.user)
        return form


admin.site.register(Animal, AdminAnimal)

admin.site.register(MetaVacuna)
admin.site.register(Raza)
admin.site.register(Especie)
