
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Seven Psychopaths", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Seven Psychopaths", 
        year=2012, 
        plot="A struggling screenwriter inadvertently becomes entangled in the Los Angeles criminal underworld after his oddball friends kidnap a gangster's beloved Shih Tzu.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    