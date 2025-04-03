
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transformers: Age of Extinction to the database
movies.insert(
    title="Transformers: Age of Extinction", 
    year=2014, 
    plot="Autobots must escape sight from a bounty hunter who has taken control of the human serendipity: Unexpectedly, Optimus Prime and his remaining gang turn to a mechanic, his daughter, and her back street racing boyfriend for help.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Transformers: Age of Extinction", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    