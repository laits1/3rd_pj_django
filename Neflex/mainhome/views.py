
from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup as Soup
import pandas as pd
from django.db.models import Count
import requests
# from .models import Movies, Ratings
# from django.contrib.auth import get_user_model
# import userfuc
from .models import Movies

# movie = Movies.objects.all()
# print(movie)



from . import myfunc
# import myfunc
# Create your views here.
def select(request):

    url = get('https://www.imdb.com/title/tt2382320/')
    req = url.text
    soup_data = Soup(req, 'html.parser')
    movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
    movie_id = 2382320
    # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
    image = movies[0].div.img['srcset'].split(',')[-4]
    # image = userfuc.image()

    # user = get_user_model().objects.get(pk=1)
    # print(user.like_movie)
    movies = Movies.objects.all()[:8]



    id = []
    title = []
    genre = []

    # for row in movies.values_list() :
    #     print(row)
    #     break
    

    context = {
        'image': image,
        'movies': movies
    }

    return render(request, "main/select.html", context)

def index(request):
  
    # a = myfunc.REC('Toy Story (1995)')
    # print(a)

    # movie_id = []

    # for i in range(4) :
    #     movie_id.append(a.index[i])

    # print(movie_id)
    # print(a.iloc[0])
    # print(a.index[0])
    # print(a.iloc)


    # context = {
    #         'movie_id': ,
    #         'movies': a
    #     }



    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        user = request.user
        # user.like_movie = ','.join(selected)
        user.save()
        
        print("gdsfafdasf")

        a = myfunc.REC('Toy Story (1995)')
        print(a)


        movie_id = []
        movies = []
        for i in range(4) :
            movie_id.append(a.index[i])
            movies.append(a.iloc[i])
        print(movie_id)


        context = {
            'movies': movies
        }




        # return render(request, "main/select copy.html", context)
        return render(request, "main/home.html", context)


    else:
        url = get('https://www.imdb.com/title/tt2382320/')
        req = url.text
        soup_data = Soup(req, 'html.parser')
        movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
        movie_id = 2382320
        # image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
        image = movies[0].div.img['srcset'].split(',')[-4]
        


        # user = get_user_model().objects.get(pk=1)
        # print(user.like_movie)
        movies = Movies.objects.all()[:6]

        movies='tt'
        # print(movies)

        context = {
            'image': image,
            'movies': movies
        }

        # movie_id2 = 2382321
        # image2 = movies[0].div.img['srcset'].split(',')[-4]
        
        return render(request, "main/index.html", context)


# def about(request):
#     return render(request, 'mainhome/about.html')


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
#     return render(request, 'mainhome/movie.html', context=context)