import os
import pickle
import pandas as pd
import streamlit as st
import requests

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

# Accessing secrets
movies_file_id = st.secrets["gdrive"]["movies_file_id"]
similarity_file_id = st.secrets["gdrive"]["similarity_file_id"]

def download_file_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        st.error(f"Error downloading {destination}: {e}")
        st.stop()

def is_valid_pickle_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            pickle.load(f)
        return True
    except Exception as e:
        st.error(f"Error validating pickle file {filepath}: {e}")
        return False

# Check if files already exist locally
if not os.path.exists('movies.pkl'):
    download_file_from_google_drive(movies_file_id, 'movies.pkl')

if not os.path.exists('similarity.pkl'):
    download_file_from_google_drive(similarity_file_id, 'similarity.pkl')

# Verify the downloaded files
if not is_valid_pickle_file('movies.pkl'):
    st.error("The downloaded movies.pkl file is not a valid pickle file.")
    st.stop()

if not is_valid_pickle_file('similarity.pkl'):
    st.error("The downloaded similarity.pkl file is not a valid pickle file.")
    st.stop()

st.header('Movie Recommender System')
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading pickle files: {e}")
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