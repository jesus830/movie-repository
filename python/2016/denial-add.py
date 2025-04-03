
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Denial to the database
movies.insert(
    title="Denial", 
    year=2016, 
    plot="Acclaimed writer and historian Deborah E. Lipstadt must battle for historical truth to prove the Holocaust actually occurred when David Irving, a renowned denier, sues her for libel.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Denial", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    