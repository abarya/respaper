# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person, Paper, person_papers, Threads

# Register your models here.

admin.site.register(Person)
admin.site.register(Paper)
admin.site.register(person_papers)
admin.site.register(Threads)