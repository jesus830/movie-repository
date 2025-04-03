
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lincoln to the database
movies.insert(
    title="Lincoln", 
    year=2012, 
    plot="As the War continues to rage, America's president struggles with continuing carnage on the battlefield as he fights with many inside his own cabinet on the decision to emancipate the slaves.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Lincoln", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    