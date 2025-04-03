
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Miss Sloane to the database
movies.insert(
    title="Miss Sloane", 
    year=2016, 
    plot="In the high-stakes world of political power-brokers, Elizabeth Sloane is the most sought after and formidable lobbyist in D.C. But when taking on the most powerful opponent of her career, she finds winning may come at too high a price.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Miss Sloane", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    