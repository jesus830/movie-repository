
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Viral", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Viral", 
        year=2016, 
        plot="Following the outbreak of a virus that wipes out the majority of the human population, a young woman documents her family's new life in quarantine and tries to protect her infected sister.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    