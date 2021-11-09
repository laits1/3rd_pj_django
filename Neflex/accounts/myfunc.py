from django.shortcuts import render
import pandas as pd
from django.db.models import Count
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random


def conn() :
    conn = sqlite3.connect("./db.sqlite3", isolation_level=None)
    c = conn.cursor()
    return c

def sel_df() :
    con = conn()
    sql = "select * from main_movies"
    con.execute(sql)
    res = con.fetchall()
    # print(type(pd.DataFrame(res)))
    M= pd.DataFrame(res)
    return pd.DataFrame(res)
# sel_df()

movies= pd.DataFrame(sel_df())
# print(data)

movies.rename(columns={0: 'movieId', 1: 'genres', 2: 'title'}, inplace=True)

# print(movies)

movies1= movies.copy()

# print(movies1)
# movies1.to_csv('moviedata.csv')


movies1.set_index('movieId', inplace= True)
# print(movies1)



# 파이썬 객체 변환을 위한 함수 선언 후 적용

def transform(a):
    return a.split('|')

movies['genres']= movies['genres'].apply(transform)

movies['genres_literal']= movies['genres'].apply(lambda x : (' ').join(x))

# 데이터 피쳐의 벡터화

count_vect= CountVectorizer(min_df= 0)
genre_mat= count_vect.fit_transform(movies['genres_literal'])

# 코사인 유사도 계산

genre_sim= cosine_similarity(genre_mat, genre_mat)
# print(genre_sim)

Genre_sim= pd.DataFrame(data= genre_sim, columns= movies.title, index= movies.title)
Genre_sim = Genre_sim.reset_index()
# print(Genre_sim)

# movieId_sim= Genre_sim.copy()
# print(movieId_sim)


# 장르가 유사한 영화 추천 함수 선언

def REC(movieId, Genre_sim=Genre_sim):
    choice = []

    movies1.loc[movieId, 'title']
    title= movies1.loc[movieId, 'title']
    # 모든 영화에 대한 해당 영화의 유사도 계산
    sim_scores = list(enumerate(Genre_sim[title]))
    # print(Genre_sim[title])
    # print(sim_scores)

    # 유사도에 따라 영화 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화 받아옴
    sim_scores = sim_scores[0:10]

    # 가장 유사한 10개 영화의 인덱스를 추출
    movie_indices = [i[0] for i in sim_scores]

    # return sim_scores

    a= []
    b= Genre_sim['title'].iloc[movie_indices]
    for i in b:
        a.append(i)
    # print(a)

    return a

# print(REC(99165))

def rec1(movieId):

    result= {}

    for id in movieId:
        s= REC(id)
        result[id]= s
    b = {}
    for value in result.values():
        for i in value:
            T = movies[movies['title'] == i]
            b[i] = ((T.movieId.tolist()[0]))
    return b

# print(rec1([99165]))
# print(rec1([99165, 104114, 158371]))

print(list(rec1([99165, 104114, 158371]).values()))

# print(dic)

# b= {}
# for value in dic.values():
#     for i in value:
#         T = movies[movies['title'] == i]
#         b[i]= ((T.movieId.tolist()[0]))

# i= 'Kid The (1921)'
# T = movies1[movies1['title'] == i]
# print(T)
# print(movies)

# print(b)
