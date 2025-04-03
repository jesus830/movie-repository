
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="My Big Fat Greek Wedding 2", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="My Big Fat Greek Wedding 2", 
        year=2016, 
        plot="A Portokalos family secret brings the beloved characters back together for an even bigger and Greeker wedding.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    