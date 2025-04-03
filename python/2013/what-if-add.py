
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add What If to the database
movies.insert(
    title="What If", 
    year=2013, 
    plot="Wallace, who is burned out from a string of failed relationships, forms an instant bond with Chantry, who lives with her longtime boyfriend. Together, they puzzle out what it means if your best friend is also the love of your life.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="What If", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    