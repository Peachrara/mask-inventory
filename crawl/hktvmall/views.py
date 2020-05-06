import os

# Create your views here.
from django.views.static import serve
from hktv import crawlHKTV
from django.shortcuts import render


def index(request):

    return render(request, 'hktvmall/index.html')

def result(request):
    filepath = os.getcwd() + "/hktv.json"
    if not os.path.isfile(filepath):
        crawlHKTV()

    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

