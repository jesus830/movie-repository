
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add King Cobra to the database
movies.insert(
    title="King Cobra", 
    year=2016, 
    plot="This ripped-from-the-headlines drama covers the early rise of gay porn headliner Sean Paul Lockhart a.k.a. Brent Corrigan, before his falling out with the producer who made him famous. When... See full summary »", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="King Cobra", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    