
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Horrible Bosses 2 to the database
movies.insert(
    title="Horrible Bosses 2", 
    year=2014, 
    plot="Dale, Kurt and Nick decide to start their own business but things don't go as planned because of a slick investor, prompting the trio to pull off a harebrained and misguided kidnapping scheme.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Horrible Bosses 2", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    