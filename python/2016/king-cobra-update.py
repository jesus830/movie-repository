
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="King Cobra", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="King Cobra", 
        year=2016, 
        plot="This ripped-from-the-headlines drama covers the early rise of gay porn headliner Sean Paul Lockhart a.k.a. Brent Corrigan, before his falling out with the producer who made him famous. When... See full summary »", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    