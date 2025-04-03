
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Toy Story 3 to the database
movies.insert(
    title="Toy Story 3", 
    year=2010, 
    plot="The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Toy Story 3", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    