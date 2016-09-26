# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    dueño = models.CharField(max_length=30)
