from django.shortcuts import render,redirect, HttpResponseRedirect

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
from django.contrib import messages
import random
from main.models import Movie_Images, Movies, Emotion, Description,Introduction
# from . import RECO
# from ..accounts import RECO




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
    

    movie_id = ['1160419','2382320','993846','120382','133093', '816692', '289043', '5052448', 
                '910970', '114709', '109830', '120338', '1675434', '2084970', '2024544', '1345836', 
                '2911666', '325980', '499549', '86190', '120737', '110357', '3783958', '361748', '120815', '253474', '112573', '118715', '405159'] # Select 페이지 선택 영화들
    images = []
    # movies = list(Movies.objects.all()[:1])
    title = []
    RandomSelect= random.sample(movie_id, 12)
    for i in range(len(RandomSelect)) :
        images.append(Movie_Images.objects.get(id=RandomSelect[i]).image)
        title.append(Movies.objects.get(id=RandomSelect[i]).title)

    # 타이틀 제목 25글자 제한
    for i in range(len(title)) : 
        if len(title[i]) > 25 :
            title[i] = title[i][:25] + "..." 

    print(images)
    print(title)

    data = list(zip(title, RandomSelect, images))
    df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])
    movies = df.to_dict('records')
  

    context = {
        # 'image': image,
        'movies1': movies[:4],
        'movies2': movies[4:8],
        'movies3': movies[8:]
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

      


        # Top
        TopMovie = ['111161', '68646', '71562', '468569', '50083', '108052', '110912', '60196', '120737', '137523', '109830', '1375666', '167261', 
        '80684', '133093', '99685', '73486', '114369', '102926', '76759', '816692','61512','57012','47396','34583','78788','120586','71315','82971','105236','86879',
        '53125','88846','71853','338013','208092','245429','118799','317248','120815','86190','361748','209144','56592','116282','435761','75314','83658','93058',
        '151804','119217','119488','910970','169547','2015381','97576','33467','106308','117951','88763','54215']
        RandomTop= random.sample(TopMovie, 8)

        images = []
        title = []
        for i in range(len(RandomTop)) :
            images.append(Movie_Images.objects.get(id=RandomTop[i]).image)
            title.append(Movies.objects.get(id=RandomTop[i]).title)

        # 타이틀 제목 25글자 제한
        for i in range(len(title)) : 
            if len(title[i]) > 25 :
                title[i] = title[i][:25] + "..." 


        data = list(zip(title, RandomTop, images))
        df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])
        movies = df.to_dict('records')

        # ComingSoon
        Coming = ['7097896', '11125620', '8110232', '11271800', '10944760', '12731980', '2382320', 
        '9812474', '11284502', '11389748', '12861508', '10665338', '4244994', '6910282', 
        '8709338', '8241000', '1160419', '8847712', '7504818', '11151336', '8956324', '15413054', '9639470', '7740510', 
        '13544716', '6992978', '10925852']
        RandomComing= random.sample(Coming, 8)

        images = []
        title = []
        for i in range(len(RandomComing)) :
            images.append(Movie_Images.objects.get(id=RandomComing[i]).image)
            title.append(Movies.objects.get(id=RandomComing[i]).title)

        # 타이틀 제목 25글자 제한
        for i in range(len(title)) : 
            if len(title[i]) > 25 :
                title[i] = title[i][:25] + "..." 

        data = list(zip(title, RandomComing, images))
        df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])

        ComingMovies = df.to_dict('records')

        # popular
        Popular = ['816692', '7286456', '1160419', '7144666', '1856101', '9376612', '8946378', '4513678', 
        '4244994', '7131622', '13544716', '9639470', '2382320', '8847712', '1457767', '3228774', '6334354']

        RandomComing= random.sample(Popular, 8)

        images = []
        title = []
        for i in range(len(RandomComing)) :
            images.append(Movie_Images.objects.get(id=RandomComing[i]).image)
            title.append(Movies.objects.get(id=RandomComing[i]).title)

        # 타이틀 제목 25글자 제한
        for i in range(len(title)) : 
            if len(title[i]) > 25 :
                title[i] = title[i][:25] + "..." 

        data = list(zip(title, RandomComing, images))
        df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])

        PopularMovies = df.to_dict('records')





        context = {
            'movies1': movies[:4],
            'movies2': movies[4:],
            'movies3': ComingMovies[:4],
            'movies4': ComingMovies[4:],
            'movies5': PopularMovies[:4],
            'movies6': PopularMovies[4:]
        }

        # movie_id2 = 2382321
        # image2 = movies[0].div.img['srcset'].split(',')[-4]
        
        return render(request, "main/home.html", context)


# def about(request):
#     return render(request, 'main/about.html')


def moviepage(request, movie_id):


    movie = Movies.objects.get(id=movie_id)
    image = Movie_Images.objects.get(id=movie_id)
    description = Description.objects.get(id=movie_id)
    introduction = Introduction.objects.get(id=movie_id)
 

    context = {
        'movie': movie,
        'image': image,
        'description' : description,
        'introduction' : introduction
    }
    return render(request, 'main/moviepage.html', context)