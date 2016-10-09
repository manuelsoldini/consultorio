# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save, post_delete, pre_save



class ModelWithImage(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=30)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.imagen))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.nombre

class Especie(ModelWithImage):
    pass
    

class Raza(ModelWithImage):
    familia = models.ForeignKey(Especie)


class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    dueño = models.CharField(max_length=60)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    descripcion = models.TextField()
    raza = models.ForeignKey(Raza)
    especie = models.ForeignKey(Especie)

    class Meta:
        verbose_name_plural = "animales"

    def __str__(self):
        return "'" + self.nombre + "': " + self.dueño + ", " +self.telefono


class Entrada(models.Model):
    fecha = models.DateField('Fecha de la visita')
    entrada = models.TextField()
    peso = models.FloatField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='entradas')
    class Meta:
        ordering = ('fecha',)

    #def pre_save(sender, instance, **kwargs):
    #    pass

class MetaVacuna(models.Model):
    nombre = models.CharField(max_length=70)
    class Meta:
        verbose_name_plural = "vacunas"
        verbose_name = "vacuna"


class Vacuna(models.Model):
    fecha = models.DateField('Fecha de vacunacion')
    vacuna = models.ForeignKey(MetaVacuna, default=None)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vacunas')
    class Meta:
        ordering = ('fecha',)



#pre_save.connect(Entrada.pre_save, Entrada, dispatch_uid="consultorio.fichas.models.Entrada")
