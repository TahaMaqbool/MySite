# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from models import Album

def index(request):
    albums = Album.objects.all()
    return render(request,'music/index.html',{'albums': albums})

def details(request,album_id):
    try:
        album = Album.objects.get(id = album_id)
    except Album.DoesNotExist:
        raise Http404("This Album does not exists!")
    return render(request,'music/detail.html',{'album':album})