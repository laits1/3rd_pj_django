from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup as Soup
import pandas as pd
from django.db.models import Count
import requests
from .models import Movies
from django.contrib.auth import get_user_model
import sqlite3


def image() :
    url = get('https://www.imdb.com/title/tt2382320/')
    req = url.text
    soup_data = Soup(req, 'html.parser')
    movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
    movie_id = 2382320
    # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
    image = movies[0].div.img['srcset'].split(',')[-4]

    return image


def movie_rec() :
    user = get_user_model().objects.get(pk=1)
    # print(user.like_movie)
    movies = Movies.objects.all()
    id = []
    title = []
    genre = []

    for row in movies.values_list() :
        print(row)
        break
    # movies = Movies.objects.all()
    # print(movies['title'])
    

    # ratings = Ratings.objects.all()[:20]
    # for row in ratings.values_list() :
    #     print(row)

 