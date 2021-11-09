from requests import get
from bs4 import BeautifulSoup as Soup
import pandas as pd
from django.db.models import Count
import requests
from .models import Movies
from django.contrib.auth import get_user_model

def get_Image() :

    movies = Movies.objects.all()[9900:9908]
    print(len(movies))
    images = []
    for i in range(len(movies)) :
        url = get('https://www.imdb.com/title/tt' + format(movies[i].id), '07')
        req = url.text
        soup_data = Soup(req, 'html.parser')
        image_tag = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
    

        # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
        images.append(image_tag[0].div.img['srcset'].split(',')[-4])


    # user = get_user_model().objects.get(pk=1)

    print("get함수", movies[0].id)
    print("함수내 이미지 : ", images)

    context = {
        'image': images,
        # 'movies': movies
    }
    return images