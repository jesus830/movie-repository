
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Hologram for the King to the database
movies.insert(
    title="A Hologram for the King", 
    year=2016, 
    plot="A failed American sales rep looks to recoup his losses by traveling to Saudi Arabia and selling his company's product to a wealthy monarch.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="A Hologram for the King", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    