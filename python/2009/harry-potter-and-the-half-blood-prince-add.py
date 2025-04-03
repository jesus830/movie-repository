
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Harry Potter and the Half-Blood Prince to the database
movies.insert(
    title="Harry Potter and the Half-Blood Prince", 
    year=2009, 
    plot="As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as "the property of the Half-Blood Prince" and begins to learn more about Lord Voldemort's dark past.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Half-Blood Prince", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    