
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Last Airbender to the database
movies.insert(
    title="The Last Airbender", 
    year=2010, 
    plot="Follows the adventures of Aang, a young successor to a long line of Avatars, who must master all four elements and stop the Fire Nation from enslaving the Water Tribes and the Earth Kingdom.", 
    rating=4.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Last Airbender", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    