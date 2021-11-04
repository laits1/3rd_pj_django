from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup as Soup
import pandas as pd
from django.db.models import Count
import requests
from .models import Movies
from django.contrib.auth import get_user_model
# import REC # REC 파이썬 폴더 사용 가능

# REC.REC()

# Create your views here.
def select(request):
    url = get('https://www.imdb.com/title/tt2382320/')
    req = url.text
    soup_data = Soup(req, 'html.parser')
    movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
    movie_id = 2382320
    # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
    image = movies[0].div.img['srcset'].split(',')[-4]
    


    user = get_user_model().objects.get(pk=1)
    print(user.like_movie)
    movies = Movies.objects.all()[:6]
    # print(movies)

    context = {
        'image': image,
        'movies': movies
    }

    return render(request, "main/select.html", context)

def home(request):
    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        user = request.user
        user.like_movie = ','.join(selected)
        user.save()
        
        return render(request, "main/home.html")


    else:
        url = get('https://www.imdb.com/title/tt2382320/')
        req = url.text
        soup_data = Soup(req, 'html.parser')
        movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
        movie_id = 2382320
        # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
        image = movies[0].div.img['srcset'].split(',')[-4]
        


        user = get_user_model().objects.get(pk=1)
        print(user.like_movie)
        movies = Movies.objects.all()[:8]
        # print(movies)

        context = {
            'image': image,
            'movies': movies
        }

        # movie_id2 = 2382321
        # image2 = movies[0].div.img['srcset'].split(',')[-4]
        
        return render(request, "main/home.html", context)


# def about(request):
#     return render(request, 'main/about.html')


# def movie(request, movie_id):

#     url = get('https://www.imdb.com/title/tt2382320/')
#     req = url.text
#     soup_data = Soup(req, 'html.parser')
#     movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
#     movie_id = 2382320
#     # movie_df = pd.read_csv("movies.csv")
   

#     title =  soup_data.findAll('div', {'class' : 'TitleBlock__SeriesParentLinkWrapper-sc-1nlhx7j-3 itQvtY'})
#     movie_title = "007 노 타임 투 다이"
#     # movie_title = movie_df.loc[movie_df["imdb_movie_Id"] == movie_id, "title"]
#     image = movies[0].div.img['srcset'].split(',')[-4]
#     context = {
#         'image': image,
#         'movie_id': movie_id,
#         'movie_title' : movie_title
#     }
#     return render(request, 'main/movie.html', context=context)