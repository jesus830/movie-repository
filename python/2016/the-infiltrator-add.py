
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Infiltrator to the database
movies.insert(
    title="The Infiltrator", 
    year=2016, 
    plot="A U.S. Customs official uncovers a money laundering scheme involving Colombian drug lord Pablo Escobar.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Infiltrator", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    