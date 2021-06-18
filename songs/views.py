from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "songs/construction.html", {
        "title": "Page in construction"
    })

def songs(request):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    }) 

def song(request, song_id):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    })

def new(request):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    })

def edit(request, song_id ):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    })

def groups(request):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    })

def grouplist(request, group_id):
     return render(request, "songs/construction.html", {
        "title": "Page in construction"
    }) 