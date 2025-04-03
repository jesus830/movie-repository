
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zodiac to the database
movies.insert(
    title="Zodiac", 
    year=2007, 
    plot="In the late 1960s/early 1970s, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Zodiac", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    