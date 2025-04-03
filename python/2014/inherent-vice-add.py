
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inherent Vice to the database
movies.insert(
    title="Inherent Vice", 
    year=2014, 
    plot="In 1970, drug-fueled Los Angeles private investigator Larry "Doc" Sportello investigates the disappearance of a former girlfriend.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Inherent Vice", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    