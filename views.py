from django.shortcuts import render
from .models import Photo
from django.http import HttpResponseRedirect


# Create your views here.

def photo_list(request):
    queryset = Photo.img.all()
    context = {"photos" : queryset}
    return render(request, "photo.html", context)


# def login(request):
#     c = {}
#     c.update(crcf(request))
#     return render_to_response('login.html', c)
#
# def aut