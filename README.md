# **Movie Recommender System**

This project is a content based recommender system which calculates the similarity matrix of 4805 movies in the TMDB database using cosine similarity. It then gives top 5 recommendations based on highest similarity scores (between -1 and 1)

![Screenshot 2024-03-17 221235](https://github.com/rohanrvpatil/movie-recommendation-system/assets/42604817/8990ac6a-d87e-4b2a-948f-f0474ba3a53b)

Project link - [Streamlit Cloud project](https://movie-recommender-system-rohanrvpatil.streamlit.app/)

If the above link doesn't work, then please follow the instructions given below from here to setup the project in your system.

### How the cosine similarity matrix was calculated:
1) The 2 .csv files in the [dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) were merged
2) All important columns were retained
3) Transformations using functions were performed to convert all column values to lists
4) The columns were merged to create a "tags" column
5) Transformations like lowercase, stemming, removing stopwords was done on the "tags" column
6) Cosine similarity matrix was calculated and a "recommend_movie" function was created to recommend the movies

### app.py workflow:
1) A PyCharm project was created with a virtual environment
2) movies.pkl and similarity.pkl files were generated from the .ipynb file itself and copied to the PyCharm project folder
3) A profile was created on [TMDB](https://www.themoviedb.org/?language=en-US) to generate an API key to fetch posters of recommended movies
4) app.py was designed to fetch posters from [TMDB](https://www.themoviedb.org/?language=en-US) and generate movie names
5) Movie names and posters were displayed
6) App was deployed to Streamlit Community Cloud

### Instructions to run project locally:
1. Clone the repository:
    ```sh
    git clone https://github.com/rohanrvpatil/movie-recommendation-system.git
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Get a TMDB API key from [here](https://developer.themoviedb.org/reference/intro/authentication) and store it in `.streamlit/secrets.toml`:
    ```toml
    # .streamlit/secrets.toml
    [general]
    tmdb_api_key = "your_tmdb_api_key"
    ```

4. Access the API key in your `app.py`:
    ```python
    import streamlit as st

    tmdb_api_key = st.secrets["general"]["tmdb_api_key"]
    # Use the API key to fetch data from TMDB
    ```

5. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```


> [!TIP]
> Use VPN if the movie recommender system is not working. API requests to TMDB from certain countries don't work


### Resources:
1) [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2) [API key creation](https://www.themoviedb.org/?language=en-US)
3) [YouTube link of project](https://www.youtube.com/watch?v=1xtrIEwY_zY&t=2s)
