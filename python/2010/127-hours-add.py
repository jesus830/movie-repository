
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 127 Hours to the database
movies.insert(
    title="127 Hours", 
    year=2010, 
    plot="An adventurous mountain climber becomes trapped under a boulder while canyoneering alone near Moab, Utah and resorts to desperate measures in order to survive.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="127 Hours", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    