# yourapp/forms.py
from django.forms import ModelForm
from .models import Animal, Vacuna
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        exclude = ['pk', ]
    class Media:
        css = {
            'all': ('hover.css',)
        }

    raza = AutoCompleteSelectField('razas')
    especie = AutoCompleteSelectField('especies')


class VacunaInlineForm(ModelForm):
    class Meta:
        model = Vacuna 
        exclude = ['pk', ]

    vacuna = AutoCompleteSelectField('vacunas')

