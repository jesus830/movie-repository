
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Crimson Peak to the database
movies.insert(
    title="Crimson Peak", 
    year=2015, 
    plot="In the aftermath of a family tragedy, an aspiring author is torn between love for her childhood friend and the temptation of a mysterious outsider. Trying to escape the ghosts of her past, she is swept away to a house that breathes, bleeds - and remembers.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Crimson Peak", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    