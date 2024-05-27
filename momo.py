import tmdbsimple
from tmdbsimple import Discover, Genres
import random

tmdbsimple.API_KEY = 'd2127d97e138fc205a054f0b00c8d863'

def get_genre_id(genre_name):
    genres = Genres()
    genre_list = genres.movie_list()['genres']
    for genre in genre_list:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None 

def get_random_movie(genre_id=None):
    discover = Discover()
    params = {'with_watch_providers': 8, 'watch_region': 'BR'}
    if genre_id:
        params['with_genres'] = genre_id

    response = discover.movie(**params)
    movies = response['results']
    if movies:
        return random.choice(movies)['title']
    else:
        return "Nenhum filme para esse gênero."

if __name__ == "__main__":
    while True:
        genre_input = input("Escolha o gênero do filme ou aperte enter: ")
        if genre_input.lower() == 'exit':
            break

        genre_id = get_genre_id(genre_input) if genre_input else None
        movie_title = get_random_movie(genre_id)
        print("O filme escolhido foi: ", movie_title)
