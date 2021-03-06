from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=300)
    genres = models.CharField(max_length=300)


class Movie_Images(models.Model):
    title = models.CharField(max_length=300)
    image = models.CharField(max_length=300)

class Links(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)


class Ratings(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_Id = models.IntegerField()
    rating = models.FloatField()

class Genome_Tags(models.Model):
    tag = models.CharField(max_length=300)
    
class Genome_Scores(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    tag_Id = models.ForeignKey(Genome_Tags, on_delete=models.CASCADE)
    relevance = models.FloatField()

class Review(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review = models.TextField()

class Tags(models.Model):
    imdb_movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_Id = models.IntegerField()
    tag = models.CharField(max_length=300)

class Director(models.Model):
    Director_name = models.CharField(max_length=300)
    movies = models.ManyToManyField(Movies)

class Actor(models.Model):
    Actor_name = models.CharField(max_length=300)
    movies = models.ManyToManyField(Movies)

class Description(models.Model):
    Description = models.TextField()

class Emotion(models.Model) :
    Happy = models.FloatField()
    Angry = models.FloatField()
    Surprise = models.FloatField()
    Sad = models.FloatField()
    Fear = models.FloatField()

class Introduction(models.Model) :
    Rating = models.FloatField()
    Director = models.CharField(max_length=100)
    Actor_list = models.CharField(max_length=100)
    