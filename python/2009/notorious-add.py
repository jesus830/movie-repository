
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Notorious to the database
movies.insert(
    title="Notorious", 
    year=2009, 
    plot="The life and death story of Notorious B.I.G. (a.k.a. Christopher Wallace), who came straight out of Brooklyn to take the world of rap music by storm.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Notorious", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    