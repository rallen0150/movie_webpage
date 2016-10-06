from django.db import models

# Create your models here.
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=30)
    video_release_date = models.CharField(max_length=30)
    imdb_url = models.CharField(max_length=150)
    unknown = models.CharField(max_length=50)
    action_genre = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()
