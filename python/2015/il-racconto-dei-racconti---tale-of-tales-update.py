
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Il racconto dei racconti - Tale of Tales", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Il racconto dei racconti - Tale of Tales", 
        year=2015, 
        plot="From the bitter quest of the Queen of Longtrellis, to two mysterious sisters who provoke the passion of a king, to the King of Highhills obsessed with a giant Flea, these tales are inspired by the fairytales by Giambattista Basile.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    