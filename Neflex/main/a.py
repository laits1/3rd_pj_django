import os
import pandas as pd


movie_df = pd.read_csv("movies.csv")
movie_id = 2382320

movie_title = movie_df.loc[movie_df["imdb_movie_Id"] == movie_id, "title"]

print(movie_title.iloc[0])

