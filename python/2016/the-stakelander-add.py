
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Stakelander to the database
movies.insert(
    title="The Stakelander", 
    year=2016, 
    plot="When his home of New Eden is destroyed by a revitalized Brotherhood and its new Vamp leader, Martin finds himself alone in the badlands of America with only the distant memory of his mentor and legendary vampire hunter, Mister, to guide him.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Stakelander", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    