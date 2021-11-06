from django.shortcuts import render
import pandas as pd
from django.db.models import Count
import sqlite3

# def REC(title, genre_sim=genre_sim):
#     choice = []
#
#     # 모든 영화에 대한 해당 영화의 유사도 계산
#     sim_scores = list(enumerate(genre_sim[title]))
#
#     # 유사도에 따라 영화 정렬
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#
#     # 가장 유사한 10개의 영화 받아옴
#     sim_scores = sim_scores[1:11]
#
#     # 가장 유사한 10개 영화의 인덱스를 추출
#     movie_indices = [i[0] for i in sim_scores]
#
#     return genre_sim['title'].iloc[movie_indices]

def conn() :
    conn = sqlite3.connect("../db.sqlite3", isolation_level=None)
    c = conn.cursor()
    return c

def sel_df() :
    con = conn()
    sql = "select * from main_movies"
    con.execute(sql)
    res = con.fetchall()
    # print(type(pd.DataFrame(res)))
    movie= pd.DataFrame(res)
    print(movie)
    return pd.DataFrame(res)
sel_df()
