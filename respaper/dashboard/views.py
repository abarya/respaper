# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Threads, Paper
# Create your views here.

def home(request):
    return render(request,'dragdrop.html')


def thread_index(request):
    all_threads = Threads.objects.all()
    thread_list = []
    thread_name = []
    for thread in all_threads:
        papers = thread.papers.split(',')
        papers = [Paper.objects.get(pk=int(paper)) for paper in papers]
        thread_list.append(papers)
        thread_name.append(thread.name)
    return render(request,'thread_index.html',context={'thread_list': thread_list,'thread_name': thread_name})