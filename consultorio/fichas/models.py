# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe


class ModelWithImage(models.Model):
    imagen = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.imagen))

    image_tag.short_description = 'Image'


class Especie(ModelWithImage):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

class Raza(ModelWithImage):
    nombre = models.CharField(max_length=30)
    especie = models.ForeignKey(Especie)

    def __unicode__(self):
        return self.nombre


class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    dueño = models.CharField(max_length=60)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    descripcion = models.TextField()
    raza = models.ForeignKey(Raza)
    especie = models.ForeignKey(Especie)

    def __unicode__(self):
        return self.nombre + self.dueño


class Entrada(models.Model):
    fecha = models.DateTimeField('fecha de la visita')
    entrada = models.TextField()
    peso = models.FloatField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='entradas')
    class Meta:
        ordering = ('fecha',)


class Vacuna(models.Model):
    fecha = models.DateTimeField('fecha de vacunacion')
    nombre = models.TextField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vacunas')
    class Meta:
        ordering = ('fecha',)
