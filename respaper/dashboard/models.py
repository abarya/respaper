# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Paper(models.Model):
    link = models.URLField(max_length=200)
    paper_name = models.CharField(max_length=200,default="paper name")

class person_papers(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)   #if an album is deleted, all its songs should get automatically deleted.
    paper_id = models.CharField(max_length=10)

class Threads(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    papers = models.CharField(max_length=200)
# Create your models here.
