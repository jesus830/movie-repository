
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Equals to the database
movies.insert(
    title="Equals", 
    year=2015, 
    plot="In an emotionless utopia, two people fall in love when they regain their feelings from a mysterious disease, causing tensions between them and their society.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Equals", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    