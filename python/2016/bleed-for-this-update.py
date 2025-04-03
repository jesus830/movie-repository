
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Bleed for This", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Bleed for This", 
        year=2016, 
        plot="The inspirational story of World Champion Boxer Vinny Pazienza who, after a near fatal car crash which left him not knowing if he'd ever walk again, made one of sport's most incredible comebacks.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    