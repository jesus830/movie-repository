
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add You Don't Mess with the Zohan to the database
movies.insert(
    title="You Don't Mess with the Zohan", 
    year=2008, 
    plot="An Israeli Special Forces Soldier fakes his death so he can re-emerge in New York City as a hair stylist.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="You Don't Mess with the Zohan", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    