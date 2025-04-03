
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Whiskey Tango Foxtrot to the database
movies.insert(
    title="Whiskey Tango Foxtrot", 
    year=2016, 
    plot="A journalist recounts her wartime coverage in Afghanistan.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Whiskey Tango Foxtrot", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    