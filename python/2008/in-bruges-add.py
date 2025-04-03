
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add In Bruges to the database
movies.insert(
    title="In Bruges", 
    year=2008, 
    plot="Guilt-stricken after a job gone wrong, hitman Ray and his partner await orders from their ruthless boss in Bruges, Belgium, the last place in the world Ray wants to be.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="In Bruges", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    