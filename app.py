import os
import pickle
import pandas as pd
import streamlit as st
import requests

from pkl_management import reassemble_file

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

    return recommended_movie_names, recommended_movie_posters



def is_valid_pickle_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            pickle.load(f)
        return True
    except Exception as e:
        st.error(f"Error validating pickle file {filepath}: {e}")
        return False


st.header('Movie Recommender System')

#Loading pickle files
movies = pickle.load(open('movies.pkl', 'rb'))
reassemble_file('similarity.pkl', 'similarity_reassembled.pkl')

if not is_valid_pickle_file('similarity_reassembled.pkl'):
    st.error("The reassembled similarity.pkl file is not a valid pickle file.")
    st.stop()

try:
    similarity = pickle.load(open('similarity_reassembled.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading reassembled similarity.pkl file: {e}")
    st.stop()


movies = pd.DataFrame(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie to generate recommendations",
    movie_list
)

if st.button('Generate', type='primary'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(recommended_movie_names[i])
        col.image(recommended_movie_posters[i])