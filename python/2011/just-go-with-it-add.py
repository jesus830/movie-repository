
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Just Go with It to the database
movies.insert(
    title="Just Go with It", 
    year=2011, 
    plot="On a weekend trip to Hawaii, a plastic surgeon convinces his loyal assistant to pose as his soon-to-be-divorced wife in order to cover up a careless lie he told to his much-younger girlfriend.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Just Go with It", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    