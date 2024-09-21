import pickle

import pandas as pd
import streamlit as st
import requests

import gdown

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5f1896dc15cb5039314227a544a51562&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

movies_file_id = '1Cf2zZ0S_BhtIZFMQe2JOuE0ILHZh5eDR'
similarity_file_id = '1UZdvcMJVMlWRZFCrelzkzP9QzqFoKU9o'

gdown.download(f'https://drive.google.com/uc?id={movies_file_id}', 'movies.pkl', quiet=False)
gdown.download(f'https://drive.google.com/uc?id={similarity_file_id}', 'similarity.pkl', quiet=False)

st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie to generate recommendations",
    movie_list
)

if st.button('Generate', type='primary'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(recommended_movie_names[i])
        col.image(recommended_movie_posters[i])





