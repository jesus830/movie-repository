
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jennifer's Body", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jennifer's Body", 
        year=2009, 
        plot="A newly possessed high school cheerleader turns into a succubus who specializes in killing her male classmates. Can her best friend put an end to the horror?", 
        rating=5.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    