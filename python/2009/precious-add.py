
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Precious to the database
movies.insert(
    title="Precious", 
    year=2009, 
    plot="In New York City's Harlem circa 1987, an overweight, abused, illiterate teen who is pregnant with her second child is invited to enroll in an alternative school in hopes that her life can head in a new direction.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Precious", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    