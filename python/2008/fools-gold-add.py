
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fool's Gold to the database
movies.insert(
    title="Fool's Gold", 
    year=2008, 
    plot="A new clue to the whereabouts of a lost treasure rekindles a married couple's sense of adventure -- and their estranged romance.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Fool's Gold", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    