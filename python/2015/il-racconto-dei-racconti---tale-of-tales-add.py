
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Il racconto dei racconti - Tale of Tales to the database
movies.insert(
    title="Il racconto dei racconti - Tale of Tales", 
    year=2015, 
    plot="From the bitter quest of the Queen of Longtrellis, to two mysterious sisters who provoke the passion of a king, to the King of Highhills obsessed with a giant Flea, these tales are inspired by the fairytales by Giambattista Basile.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Il racconto dei racconti - Tale of Tales", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    