
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Everybody Wants Some!! to the database
movies.insert(
    title="Everybody Wants Some!!", 
    year=2016, 
    plot="In 1980, a group of college baseball players navigate their way through the freedoms and responsibilities of unsupervised adulthood.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Everybody Wants Some!!", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    