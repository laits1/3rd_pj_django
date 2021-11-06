# import os
# import django
# import csv
# import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# # system setup
# os.chdir('.')
# # print('Current dir의 경로 : ', end=''), print(os.getcwd())               # os가 파악한 현재 경로를 표기
# # print('os.path.abspath(__file__)의 경로 : ',os.path.abspath(__file__))    # 현재 작업중인 파일을 포함 경로를 구체적으로 표기
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # print('BASE_DIR=', end=''), print(BASE_DIR)
# # print('똑같나? 다르나?', BASE_DIR == os.getcwd()) # 소문자 c , 대문자 C 차이 때문인것 같네요.

# sys.path.append(BASE_DIR)  # sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. sys에 대해서는 뒤에서 자세하게 다룰 것이다. 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Neflex.settings') 
#  # python이 실행될 때 DJANGO_SETTINGS_MODULE라는 환경 변수에
# # 현재 프로젝트의 settings.py 파일 경로를 등록
# django.setup() # python manage.py shell 을 실행하는 것이랑 비슷한 방법이다. 즉 파이썬 파일에서도 django를 실행 시킬수 있다.

# # import model
from mainhome.models import *

movies = Movies.objects.all()

movieId = []
title = []
genres = []
for movie in movies :
    # print(f'번호 : {movie.id}\t, 타이틀 : {movie.title}\t\t\t\t\t\t, 장르 : {movie.genres}')
    movieId.append(movie.id)
    title.append(movie.title)
    genres.append(movie.genres)
    

# print(len(movieId))
# print(len(title))
# print(len(genres))

data = list(zip(movieId, title, genres))
movies = pd.DataFrame(data, columns = ['movieId', 'title', 'genres'])
# print(movies)



def transform(a):
    return a.split('|')


movies['genres'] = movies['genres'].apply(transform)

movies['genres_literal'] = movies['genres'].apply(lambda x: (' ').join(x))

# 데이터 피쳐의 벡터화

count_vect = CountVectorizer(min_df=0)
genre_mat = count_vect.fit_transform(movies['genres_literal'])

# 코사인 유사도 계산

genre_sim = cosine_similarity(genre_mat, genre_mat)
# print(genre_sim)

Genre_sim = pd.DataFrame(data=genre_sim, columns=movies.title, index=movies.title)
Genre_sim = Genre_sim.reset_index()


# print(Genre_sim)

# 장르가 유사한 영화 추천 함수 선언

def REC(title, Genre_sim=Genre_sim):
    choice = []

    # 모든 영화에 대한 해당 영화의 유사도 계산
    sim_scores = list(enumerate(Genre_sim[title]))
    # print(type(Genre_sim[title]))
    # 유사도에 따라 영화 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화 받아옴
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개 영화의 인덱스를 추출
    movie_indices = [i[0] for i in sim_scores]

    return Genre_sim['title'].iloc[movie_indices]

a = REC('Toy Story (1995)')

print(a.iloc[1])

# print(movieId)

# import pymysql

# host = "localhost" #접속할 db의 host명
# user = "root" #접속할 db의 user명
# pw = "0000" #접속할 db의 password
# db = "neflex" #접속할 db의 table명 (실제 데이터가 추출되는 table)

# conn = pymysql.connect( host= host, user = user, password = pw, db = db)

# #실제 사용 될 sql쿼리 문
# sql = "SELECT * FROM mainhome_movies LIMIT 10"

# #sql문 실행 / 데이터 받기
# curs = conn.cusor()
# curs.execute(sql)

# data = curs.fetchall()

# print(data)

# #db 접속 종료
# curs.close()
# conn.close()

# import pandas as pd
# from sqlalchemy import create_engine

# engine = create_engine('mysql://root:0000@localhost/neflex', convert_unicode=True)
# conn = engine.connect()

# data = pd.read_sql_table('mainhome_movies', conn)
# print(data.head())

# print(data['id'])