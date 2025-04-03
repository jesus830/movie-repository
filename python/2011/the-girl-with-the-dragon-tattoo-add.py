
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Girl with the Dragon Tattoo to the database
movies.insert(
    title="The Girl with the Dragon Tattoo", 
    year=2011, 
    plot="Journalist Mikael Blomkvist is aided in his search for a woman who has been missing for forty years by Lisbeth Salander, a young computer hacker.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Girl with the Dragon Tattoo", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    