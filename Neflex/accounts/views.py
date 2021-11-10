from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from pandas.core.frame import DataFrame
import requests
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
import pandas as pd
from main.models import Movie_Images, Movies
from .forms import CustomCreationForm

from django.contrib import auth
from . import myfunc, RECO
import random
# Create your views here.
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)

def after_login(request):
    if request.method == 'POST':
        print("영화저장성공")
        selected = request.POST.getlist('selected')
        user = request.user
        user.like_movie = ','.join(selected)
        user.save()
    
        # print("유저가 선택한 영화 번호 : ", user.like_movie.split(',')[0])    
    user = request.user 


    u1 = int(user.like_movie.split(',')[0])
    u2 = int(user.like_movie.split(',')[1])
    u3 = int(user.like_movie.split(',')[2])

    ## 세웅님 추천 알고리즘

    u1_title = Movies.objects.get(id=u1).title
    print("u1타이틀 : ", u1_title)
    # a = RECO.get_movie_recommendation(u1_title).Title.tolist()
    # print("a : " , a)







    # 서응님 추천 알고리즘
    movieId = list(myfunc.rec1([u1, u2, u3]).values())
    di= myfunc.rec1([u1, u2, u3])
    movietitle = list(myfunc.rec1([u1, u2, u3]).keys())
    recomend= random.sample(movieId, 8)
    randommovietitle= []
    

    for i in recomend:
        
        randommovietitle.append(find_key(di, i)[:20])

    movieImage = []
   
    for i in range(8) :
        movieImage.append(Movie_Images.objects.get(id=recomend[i]).image)

    print(randommovietitle)     # 추천결과 영화 제목
    print(recomend)             # 추천결과 영화 번호
    print(movieImage)           # 추천결과 영화 이미지 주소

    # 타이틀 제목 25글자 제한
    for i in range(len(randommovietitle)) : 
        if len(randommovietitle[i]) > 25 :
            randommovietitle[i] = randommovietitle[i][:25] + "..." 


    data = list(zip(randommovietitle, recomend, movieImage))
    df = pd.DataFrame(data, columns = ['title', 'movie_id', 'image'])
    movies = df.to_dict('records')

    
    # Top
    TopMovie = ['111161', '68646', '71562', '468569', '50083', '108052', '110912', '60196', '120737', '137523', '109830', '1375666', '167261', 
    '80684', '133093', '99685', '73486', '114369', '102926', '76759', '816692']
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
    Topmovies = df.to_dict('records')

    context = {
        'movies1': movies[:4],
        'movies2': movies[4:],
        'movies3': Topmovies[:4],
        'movies4': Topmovies[4:]
    }
    return render(request, 'accounts/after_login_page.html', context)


def login(request) :

    if request.method == 'POST' :

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None : # 올바른 아이디로 접속하면
            auth.login(request, user)
            if user.like_movie:
                return redirect('accounts:after_login')
            return redirect('main:select')
        else :
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else :
        return render(request, 'accounts/login.html')


def logout(request) :
    auth.logout(request)
    return redirect('accounts:login')

def home(request) :
    return render(request, 'accounts/login.html')


def signup(request) :
    # 회원가입 화면에서 회원가입 버튼 눌렀을 때
    if request.method == 'POST':
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@post?')
        username = request.POST.get('name')
        password = request.POST.get('password')
        print(request.POST)
        # print(username, password)

        user_info = {
            'csrfmiddlewaretoken' : request.POST.get('csrfmiddlewaretoken'),
            'username' : username,
            'password1' : password,
            'password2' : password 
        }

        print(user_info)


        form = CustomCreationForm(user_info)       # 직접만든 폼
        # form = CustomCreationForm(request.POST)  # 제공폼
        
        if form.is_valid():
            print("form 유효?")
            form.save()
            return redirect('accounts:login')

        
        context={'form':form}
        
        return render(request, 'accounts/signup.html', context)


    # 회원가입 완료 후 -> 로그인 페이지로 갈 때
    else:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@no post?')
        form = CustomCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)