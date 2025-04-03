
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add RocknRolla to the database
movies.insert(
    title="RocknRolla", 
    year=2008, 
    plot="In London, a real-estate scam puts millions of pounds up for grabs, attracting some of the city's scrappiest tough guys and its more established underworld types, all of whom are looking to get rich quick. While the city's seasoned criminals vie for the cash, an unexpected player -- a drugged-out rock 'n' roller presumed to be dead but very much alive -- has a multi-million-dollar prize fall into... See full summary »", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="RocknRolla", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    