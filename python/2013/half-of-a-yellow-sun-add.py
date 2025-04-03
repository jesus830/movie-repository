
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Half of a Yellow Sun to the database
movies.insert(
    title="Half of a Yellow Sun", 
    year=2013, 
    plot="Sisters Olanna and Kainene return home to 1960s Nigeria, where they soon diverge on different paths. As civil war breaks out, political events loom larger than their differences as they join the fight to establish an independent republic.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Half of a Yellow Sun", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    