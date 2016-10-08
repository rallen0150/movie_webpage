from django.shortcuts import render

from django.http import HttpResponse
from movieratings.models import Rater, Movie, Rating
from django.db.models import Avg

# Create your views here.

def index_view(request):
    context = {
        "title": "Movie Data!",
    }
    return render(request, "index.html", context)

def top_20_view(request):
    context = {
        "top_20": Movie.objects.annotate(top_rating=Avg('rating__rating')).order_by('-top_rating')[:20]
    }
    return render(request, "top_20_movies.html", context)

def movie_view(request):
    context = {
        "all_movies": Movie.objects.all(),
    }
    return render(request, "movies.html", context)

def film_info(request, movie_id):
    context ={
        "movie": Movie.objects.get(id=movie_id),
        "info": Rating.objects.filter(movie=movie_id)
    }
    return render(request, "film.html", context)

def user_view(request):
    context = {
        "all_users": Rater.objects.all()
    }
    return render(request, "users.html", context)

def rater_info(request, rater_id):
    context ={
        "info": Rater.objects.get(id=rater_id),
        "movies": Rating.objects.filter(user=rater_id)
    }
    return render(request, "rater.html", context)
