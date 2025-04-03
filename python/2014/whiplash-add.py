
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Whiplash to the database
movies.insert(
    title="Whiplash", 
    year=2014, 
    plot="A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Whiplash", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    