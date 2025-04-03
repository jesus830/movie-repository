
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hunt for the Wilderpeople to the database
movies.insert(
    title="Hunt for the Wilderpeople", 
    year=2016, 
    plot="A national manhunt is ordered for a rebellious kid and his foster uncle who go missing in the wild New Zealand bush.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Hunt for the Wilderpeople", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    