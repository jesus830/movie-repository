
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Everybody Wants Some!!", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Everybody Wants Some!!", 
        year=2016, 
        plot="In 1980, a group of college baseball players navigate their way through the freedoms and responsibilities of unsupervised adulthood.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    