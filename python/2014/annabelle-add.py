
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Annabelle to the database
movies.insert(
    title="Annabelle", 
    year=2014, 
    plot="A couple begins to experience terrifying supernatural occurrences involving a vintage doll shortly after their home is invaded by satanic cultists.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Annabelle", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    