
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Man Down", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Man Down", 
        year=2015, 
        plot="In a post-apocalyptic America, former U.S. Marine Gabriel Drummer searches desperately for the whereabouts of his son, accompanied by his best friend and a survivor.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    