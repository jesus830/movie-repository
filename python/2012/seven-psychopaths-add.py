
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Seven Psychopaths to the database
movies.insert(
    title="Seven Psychopaths", 
    year=2012, 
    plot="A struggling screenwriter inadvertently becomes entangled in the Los Angeles criminal underworld after his oddball friends kidnap a gangster's beloved Shih Tzu.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Seven Psychopaths", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    