
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Secret in Their Eyes to the database
movies.insert(
    title="Secret in Their Eyes", 
    year=2015, 
    plot="A tight-knit team of rising investigators, along with their supervisor, is suddenly torn apart when they discover that one of their own teenage daughters has been brutally murdered.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Secret in Their Eyes", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    