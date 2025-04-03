
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Chef to the database
movies.insert(
    title="Chef", 
    year=2014, 
    plot="A head chef quits his restaurant job and buys a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Chef", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    