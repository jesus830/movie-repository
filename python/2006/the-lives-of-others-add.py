
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lives of Others to the database
movies.insert(
    title="The Lives of Others", 
    year=2006, 
    plot="In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lives of Others", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    