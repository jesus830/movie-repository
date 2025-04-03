
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Self/less to the database
movies.insert(
    title="Self/less", 
    year=2015, 
    plot="A dying real estate mogul transfers his consciousness into a healthy young body, but soon finds that neither the procedure nor the company that performed it are quite what they seem.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Self/less", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    