
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Turbo Kid", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Turbo Kid", 
        year=2015, 
        plot="In a post-apocalyptic wasteland in 1997, a comic book fan adopts the persona of his favourite hero to save his enthusiastic friend and fight a tyrannical overlord.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    