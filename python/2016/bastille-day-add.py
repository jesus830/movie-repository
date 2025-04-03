
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bastille Day to the database
movies.insert(
    title="Bastille Day", 
    year=2016, 
    plot="A young con artist and an unruly CIA agent embark on an anti-terrorist mission in France.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Bastille Day", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    