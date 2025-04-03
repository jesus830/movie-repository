
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bleed for This to the database
movies.insert(
    title="Bleed for This", 
    year=2016, 
    plot="The inspirational story of World Champion Boxer Vinny Pazienza who, after a near fatal car crash which left him not knowing if he'd ever walk again, made one of sport's most incredible comebacks.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Bleed for This", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    