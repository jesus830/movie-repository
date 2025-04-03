
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The King's Speech to the database
movies.insert(
    title="The King's Speech", 
    year=2010, 
    plot="The story of King George VI of the United Kingdom of Great Britain and Northern Ireland, his impromptu ascension to the throne and the speech therapist who helped the unsure monarch become worthy of it.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="The King's Speech", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    