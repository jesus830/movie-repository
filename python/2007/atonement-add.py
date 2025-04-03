
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Atonement to the database
movies.insert(
    title="Atonement", 
    year=2007, 
    plot="Fledgling writer Briony Tallis, as a thirteen-year-old, irrevocably changes the course of several lives when she accuses her older sister's lover of a crime he did not commit.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Atonement", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    