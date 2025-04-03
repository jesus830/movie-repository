
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Woman in Gold to the database
movies.insert(
    title="Woman in Gold", 
    year=2015, 
    plot="Maria Altmann, an octogenarian Jewish refugee, takes on the Austrian government to recover artwork she believes rightfully belongs to her family.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Woman in Gold", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    