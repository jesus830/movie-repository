
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add La vie d'Adèle to the database
movies.insert(
    title="La vie d'Adèle", 
    year=2013, 
    plot="Adèle's life is changed when she meets Emma, a young woman with blue hair, who will allow her to discover desire and to assert herself as a woman and as an adult. In front of others, Adèle grows, seeks herself, loses herself, and ultimately finds herself through love and loss.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="La vie d'Adèle", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    