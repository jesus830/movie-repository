
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fantastic Four to the database
movies.insert(
    title="Fantastic Four", 
    year=2015, 
    plot="Four young outsiders teleport to an alternate and dangerous universe which alters their physical form in shocking ways. The four must learn to harness their new abilities and work together to save Earth from a former friend turned enemy.", 
    rating=4.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Fantastic Four", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    