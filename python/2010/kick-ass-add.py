
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kick-Ass to the database
movies.insert(
    title="Kick-Ass", 
    year=2010, 
    plot="Dave Lizewski is an unnoticed high school student and comic book fan who one day decides to become a superhero, even though he has no powers, training or meaningful reason to do so.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Kick-Ass", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    