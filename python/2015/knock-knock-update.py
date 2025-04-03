
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Knock Knock", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Knock Knock", 
        year=2015, 
        plot="A devoted father helps two stranded young women who knock on his door, but his kind gesture turns into a dangerous seduction and a deadly game of cat and mouse.", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    