
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Girl with the Dragon Tattoo", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Girl with the Dragon Tattoo", 
        year=2011, 
        plot="Journalist Mikael Blomkvist is aided in his search for a woman who has been missing for forty years by Lisbeth Salander, a young computer hacker.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    