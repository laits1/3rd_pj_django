# from django.shortcuts import render
# import pandas as pd
# from django.db.models import Count
# import sqlite3
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


# def conn():
#     conn = sqlite3.connect("../db.sqlite3", isolation_level=None)
#     c = conn.cursor()
#     return c


# def sel_df():
#     con = conn()
#     sql = "select * from main_movies"
#     con.execute(sql)
#     res = con.fetchall()
#     # print(type(pd.DataFrame(res)))
#     M = pd.DataFrame(res)
#     return pd.DataFrame(res)


# # sel_df()

# movies = pd.DataFrame(sel_df())
# # print(data)

# movies.rename(columns={0: 'movieId', 1: 'title', 2: 'genres'}, inplace=True)


# # print(movies)

# # 파이썬 객체 변환을 위한 함수 선언 후 적용

# def transform(a):
#     return a.split('|')


# movies['genres'] = movies['genres'].apply(transform)

# movies['genres_literal'] = movies['genres'].apply(lambda x: (' ').join(x))

# # 데이터 피쳐의 벡터화

# count_vect = CountVectorizer(min_df=0)
# genre_mat = count_vect.fit_transform(movies['genres_literal'])

# # 코사인 유사도 계산

# genre_sim = cosine_similarity(genre_mat, genre_mat)
# # print(genre_sim)

# Genre_sim = pd.DataFrame(data=genre_sim, columns=movies.title, index=movies.title)
# Genre_sim = Genre_sim.reset_index()


# # print(Genre_sim)

# # 장르가 유사한 영화 추천 함수 선언

# def REC(title, Genre_sim=Genre_sim):
#     choice = []

#     # 모든 영화에 대한 해당 영화의 유사도 계산
#     sim_scores = list(enumerate(Genre_sim[title]))
#     # print(type(Genre_sim[title]))
#     # 유사도에 따라 영화 정렬
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     # 가장 유사한 10개의 영화 받아옴
#     sim_scores = sim_scores[1:11]

#     # 가장 유사한 10개 영화의 인덱스를 추출
#     movie_indices = [i[0] for i in sim_scores]

#     return Genre_sim['title'].iloc[movie_indices]


# a = REC('Toy Story (1995)')
# print(a.iloc[1])
