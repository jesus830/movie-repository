
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Saving Mr. Banks to the database
movies.insert(
    title="Saving Mr. Banks", 
    year=2013, 
    plot="Author P.L. Travers reflects on her childhood after reluctantly meeting with Walt Disney, who seeks to adapt her Mary Poppins books for the big screen.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Saving Mr. Banks", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    