
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jennifer's Body to the database
movies.insert(
    title="Jennifer's Body", 
    year=2009, 
    plot="A newly possessed high school cheerleader turns into a succubus who specializes in killing her male classmates. Can her best friend put an end to the horror?", 
    rating=5.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Jennifer's Body", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    