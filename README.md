#**Movie Recommender System**

This project is a content based recommender system which calculates the similarity matrix of 4805 movies in the TMDB databases using cosine similarity. It then gives top 5 recommendations based on highest similarity scores (between -1 and 1)

##How the cosine similarity matrix was calculated:
1) The 2 .csv files in the dataset [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](url) were merged
2) All important columns were retained
3) Transformations using functions were performed to convert all column values to lists
4) The columns were merged to create a "tags" column
5) Transformations like lowercase, stemming, removing stopwords was done on the "tags" column
6) Cosine similarity matrix was calculated and a "recommend_movie" function was created to recommend the movies

##app.py workflow:
1) A PyCharm project was created with a virtual environment
2) movies.pkl and similarity.pkl files were generated from the .ipynb file itself and copied to the PyCharm project folder
3) A profile was created on [https://www.themoviedb.org/?language=en-US](url) to generate an API key to fetch posters of recommended movies
4) app.py was designed to fetch posters from [https://www.themoviedb.org/?language=en-US](url) and generate movie names
5) Movie names and posters were displayed
6) App was deployed to Heroku using this blog [https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd](url)

##Instructions to set up project (in brief):
1) Download dataset from [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](url)
2) Run the .ipynb file to generate movies.pkl and similarity.pkl
3) Create a new project with a virtual environment in PyCharm
4) Copy the .pkl files to the project folder
5) Run the app locally using "streamlit run app.py"
6) Deploy on Heroku by following the steps in this blog [https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd](url)

Resources:
1) TMDB 5000 Movie Dataset - [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](url)
2) API key creation - [https://www.themoviedb.org/?language=en-US](url)
3) Heroku deployment - [https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd](url)
4) Project referred from - [https://www.youtube.com/watch?v=1xtrIEwY_zY&t=2s](url)
