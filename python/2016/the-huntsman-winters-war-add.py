
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Huntsman: Winter's War to the database
movies.insert(
    title="The Huntsman: Winter's War", 
    year=2016, 
    plot="Eric and fellow warrior Sara, raised as members of ice Queen Freya's army, try to conceal their forbidden love as they fight to survive the wicked intentions of both Freya and her sister Ravenna.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Huntsman: Winter's War", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    