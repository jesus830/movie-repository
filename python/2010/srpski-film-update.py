
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Srpski film", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Srpski film", 
        year=2010, 
        plot="An aging porn star agrees to participate in an "art film" in order to make a clean break from the business, only to discover that he has been drafted into making a pedophilia and necrophilia themed snuff film.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    