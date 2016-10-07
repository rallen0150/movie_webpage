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
        "title": "Top 20 Movies Rated By Users",
        # "top_20": movie_list
    }
    return render(request, "top_20_movies.html", context)

def movie_view(request):

    context = {
        "all_movies": Movie.objects.all(),

    }
    return render(request, "movies.html", context)

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
