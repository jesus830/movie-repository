
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Legend of Tarzan to the database
movies.insert(
    title="The Legend of Tarzan", 
    year=2016, 
    plot="Tarzan, having acclimated to life in London, is called back to his former home in the jungle to investigate the activities at a mining encampment.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Legend of Tarzan", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    