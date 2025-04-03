
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Atonement", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Atonement", 
        year=2007, 
        plot="Fledgling writer Briony Tallis, as a thirteen-year-old, irrevocably changes the course of several lives when she accuses her older sister's lover of a crime he did not commit.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    