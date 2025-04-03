
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Legend of Tarzan", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Legend of Tarzan", 
        year=2016, 
        plot="Tarzan, having acclimated to life in London, is called back to his former home in the jungle to investigate the activities at a mining encampment.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    