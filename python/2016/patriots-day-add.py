
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Patriots Day to the database
movies.insert(
    title="Patriots Day", 
    year=2016, 
    plot="The story of the 2013 Boston Marathon bombing and the aftermath, which includes the city-wide manhunt to find the terrorists responsible.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Patriots Day", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    