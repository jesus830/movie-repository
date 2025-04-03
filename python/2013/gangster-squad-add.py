
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gangster Squad to the database
movies.insert(
    title="Gangster Squad", 
    year=2013, 
    plot="It's 1949 Los Angeles, the city is run by gangsters and a malicious mobster, Mickey Cohen. Determined to end the corruption, John O'Mara assembles a team of cops, ready to take down the ruthless leader and restore peace to the city.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Gangster Squad", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    