
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Denial", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Denial", 
        year=2016, 
        plot="Acclaimed writer and historian Deborah E. Lipstadt must battle for historical truth to prove the Holocaust actually occurred when David Irving, a renowned denier, sues her for libel.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    