
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Social Network to the database
movies.insert(
    title="The Social Network", 
    year=2010, 
    plot="Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Social Network", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    