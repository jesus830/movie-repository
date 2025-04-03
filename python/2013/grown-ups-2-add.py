
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Grown Ups 2 to the database
movies.insert(
    title="Grown Ups 2", 
    year=2013, 
    plot="After moving his family back to his hometown to be with his friends and their kids, Lenny finds out that between old bullies, new bullies, schizo bus drivers, drunk cops on skis, and 400 costumed party crashers sometimes crazy follows you.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Grown Ups 2", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    