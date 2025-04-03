
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Viral to the database
movies.insert(
    title="Viral", 
    year=2016, 
    plot="Following the outbreak of a virus that wipes out the majority of the human population, a young woman documents her family's new life in quarantine and tries to protect her infected sister.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Viral", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    