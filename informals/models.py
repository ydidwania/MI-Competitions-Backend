# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class InformalsGenre(models.Model):
    genre = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.genre

class Informal(models.Model):
    description = models.TextField()
    genres = InformalsGenre.objects.all()

class InformalsEvent(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.ForeignKey(InformalsGenre, on_delete = models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name