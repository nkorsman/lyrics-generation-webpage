# Spotify Top 200 Lyrics Generator

Live at:

[damp-harbor-56160.herokuapp.com](https://damp-harbor-56160.herokuapp.com/)

Docker:

    docker run -p 5000:5000 hd4niel/lyricsgen
    runnig at: http://0.0.0.0:5000/
link: https://cloud.docker.com/u/hd4niel/repository/docker/hd4niel/lyricsgen

Else, clone and run locally:

    python main.py

Dependencies can be found in requirements.txt

The model is trained on Spotify top 200 tracks 2017-2019. Data retrieval and training is done in this repo: [github.com/hd4niel/Predict-Spotify-Top200](https://github.com/hd4niel/Predict-Spotify-Top200)
