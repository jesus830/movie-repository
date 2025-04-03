
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add My Big Fat Greek Wedding 2 to the database
movies.insert(
    title="My Big Fat Greek Wedding 2", 
    year=2016, 
    plot="A Portokalos family secret brings the beloved characters back together for an even bigger and Greeker wedding.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="My Big Fat Greek Wedding 2", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    