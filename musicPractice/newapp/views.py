from django.shortcuts import render
from newapp.models import *
from .forms import *

# Create your views here.

def homepage(request):
    diction = {'text': 'This is Home Page'}
    return render (request, 'newapp/home.html', context = diction)

def band_page(request):
    band_all = Band.objects.all()
    diction = {'text':'This is the band list', 'band':band_all}
    return render (request, 'newapp/index.html', context = diction)

def album_page(request):
    album_all = Album.objects.all()
    diction = {'text':'This is the album list', 'album':album_all}
    return render (request, 'newapp/index_album.html', context = diction)


def create_band(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        form.save()
        return render(request, 'newapp/message.html')
    
    else:
        form = BandForm()
        context = {'form': form}
        return render(request, 'newapp/create_band.html', context)

def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        form.save()
        return render(request, 'newapp/message.html')
    
    else:
        form = AlbumForm()
        context = {'form': form}
        return render(request, 'newapp/create_album.html', context)
