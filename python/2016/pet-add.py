
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pet to the database
movies.insert(
    title="Pet", 
    year=2016, 
    plot="A psychological thriller about a man who bumps into an old crush and subsequently becomes obsessed with her, leading him to hold her captive underneath the animal shelter where he works. ... See full summary »", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Pet", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    