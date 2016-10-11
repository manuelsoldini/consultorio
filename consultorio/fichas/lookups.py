# yourapp/lookups.py
from ajax_select import register, LookupChannel
from .models import *

@register('razas')
class RazasLookup(LookupChannel):
    model = Raza

    def get_query(self, q, request):
        return self.model.objects.filter(nombre__icontains=q).order_by('nombre')[:50]

    def format_match(self, item):
        return u"""<div class='hover_img'>
                    <p> %s 
                       <span><img src="/media/%s" alt="image" height="100" /></span>
                    </p>
                   </div>""" % (item.nombre, item.imagen)

    def format_item_display(self, item):
        return u"""<div class='hover_img'>
                    <p> %s 
                       <span><img src="/media/%s" alt="image" height="100" /></span>
                    </p>
                   </div>""" % (item.nombre, item.imagen)


@register('especies')
class EspeciesLookup(LookupChannel):
    model = Especie

    def get_query(self, q, request):
        return self.model.objects.filter(nombre__icontains=q).order_by('nombre')[:50]

    def format_match(self, item):
        return u"""<div class='hover_img'>
                    <p> %s 
                       <span><img src="/media/%s" alt="image" height="100" /></span>
                    </p>
                   </div>""" % (item.nombre, item.imagen)


    def format_item_display(self, item):
        return u"""<div class='hover_img'>
                    <p> %s 
                       <span><img src="/media/%s" alt="image" height="100" /></span>
                    </p>
                   </div>""" % (item.nombre, item.imagen)


@register('vacunas')
class VacunasLookup(LookupChannel):
    model = MetaVacuna

    def get_query(self, q, request):
        return self.model.objects.filter(nombre__icontains=q).order_by('nombre')[:50]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.nombre


