
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Srpski film to the database
movies.insert(
    title="Srpski film", 
    year=2010, 
    plot="An aging porn star agrees to participate in an "art film" in order to make a clean break from the business, only to discover that he has been drafted into making a pedophilia and necrophilia themed snuff film.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Srpski film", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    