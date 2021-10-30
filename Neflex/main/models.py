from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)


class Links(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)


class Ratings(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField()

class Genome_Tags(models.Model):
    tag = models.CharField(max_length=100)
    
class Genome_Scores(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    tag_Id = models.ForeignKey(Genome_Tags, on_delete=models.CASCADE)
    relevance = models.FloatField()

class Review(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review = models.TextField()

class Tags(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class Director(models.Model):
    Director_name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movies)

class Actor(models.Model):
    Actor_name = models.CharField(max_length=100)
    movies = models.ManyToManyField
