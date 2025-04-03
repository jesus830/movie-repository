
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dredd to the database
movies.insert(
    title="Dredd", 
    year=2012, 
    plot="In a violent, futuristic city where the police have the authority to act as judge, jury and executioner, a cop teams with a trainee to take down a gang that deals the reality-altering drug, SLO-MO.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Dredd", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    