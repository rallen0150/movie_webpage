from django.shortcuts import render

from django.http import HttpResponse
from movieratings.models import Rater, Movie, Rating

# Create your views here.

def index_view(request):
    context = {
        "title": "Movie Data!",
    }
    return render(request, "index.html", context)

def movie_view(request, movie_id):
    context = {
        "all_movies": Movie.objects.all()
    }
    return render(request, "movies.html", context)
