from django.shortcuts import render,redirect

import pandas as pd
from django.db.models import Count

from .models import Movie_Images, Movies
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from requests import get
from bs4 import BeautifulSoup as Soup
from django.contrib import auth
# Create your views here.
from . import movieimage


def select(request):
    if request.method == 'POST':
        print("로그인성공@@")
        # selected = request.POST.getlist('selected')
        # user = request.user
        # user.like_movie = ','.join(selected)
        # user.save()

        # return render(request, "main/select.html")
    else : 
        print("로그인 post 실패")
    

    movie_id = ['1160419','2382320','0993846','0120382','0133093', '0816692', '0289043', '5052448', '0910970', '0114709', '0109830', '0120338'] # Select 페이지 선택 영화들
    images = []
    # movies = list(Movies.objects.all()[:1])
    title = []
    for i in range(len(movie_id)) :
        images.append(Movie_Images.objects.get(id=movie_id[i]).image)
        title.append(Movies.objects.get(id=movie_id[i]).title)

    print(images)
    print(title)

    data = list(zip(title, movie_id, images))
    df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])
    movies = df.to_dict('records')
  

    context = {
        # 'image': image,
        'movies1': movies[:6],
        'movies2': movies[6:]
    }
    

    return render(request, "main/select.html", context)

def home(request):
    if request.method == 'POST':
        print("로그인성공")

        selected = request.POST.getlist('selected')
        user = request.user
        user.like_movie = ','.join(selected)
        user.save()



        
        return render(request, "main/home.html")


    else:
        print("홈 함수 실행")



        # image = movieimage.get_Image()
        url = get('https://www.imdb.com/title/tt2382320/')
        req = url.text
        soup_data = Soup(req, 'html.parser')
        movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
        movie_id = 2382320
        # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
        image = movies[0].div.img['srcset'].split(',')[-4]

        print(image)
       
        movies1 = Movies.objects.all()[:4]
        movies2 = Movies.objects.all()[4:8]
        
        # print(movies[0].title)
        # print(movies)

        context = {
            'image': image,
            'movies1': movies1,
            'movies2': movies2
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