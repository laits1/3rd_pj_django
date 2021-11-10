from django.shortcuts import render
import pandas as pd
from django.db.models import Count
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


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

def sel_df1() :
    con = conn()
    sql = "select * from main_ratings"
    con.execute(sql)
    res = con.fetchall()
    # print(type(pd.DataFrame(res)))
    M= pd.DataFrame(res)
    return pd.DataFrame(res)

movies= pd.DataFrame(sel_df())
ratings= pd.DataFrame(sel_df1())

movies.rename(columns= {0: 'movieId', 1: 'genres', 2: 'title'},
              inplace= True)

ratings.rename(columns= {1: 'rating', 2: 'movieId', 3: 'userId'},
               inplace= True)

ratings.drop(labels= 0, axis= 1, inplace= True)

# print(movies)
# print(ratings)

# ratings.to_csv('ratings.csv')
# ratings = pd.read_csv('./ratings.csv')

# print(ratings.info())

final_dataset= (pd.pivot_table(ratings, index='movieId', columns='userId',
                               values='rating', aggfunc=np.sum))

final_dataset.fillna(0,inplace=True)
# print(final_dataset.head())


no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

final_dataset=final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]
# print(final_dataset)

csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)

knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)


# sample = np.array([[0,0,3,0,0],[4,0,0,0,2],[0,0,0,0,1]])
# sparsity = 1.0 - ( np.count_nonzero(sample) / float(sample.size) )
# print(sparsity)

def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies[movies['title'].str.contains(movie_name)]
    if len(movie_list):
        movie_idx= movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx],
                                             n_neighbors=n_movies_to_reccomend+1)
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),
                                            distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title':movies.iloc[idx]['title'].values[0],'Distance':val[1]})
        df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_reccomend+1))
        return df
    else:
        return "영화가 없습니다. 다시 선택해주세요"

# print(get_movie_recommendation('Iron Man').Title.tolist())

