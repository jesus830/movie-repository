
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add John Carter to the database
movies.insert(
    title="John Carter", 
    year=2012, 
    plot="Transported to Barsoom, a Civil War vet discovers a barren planet seemingly inhabited by 12-foot tall barbarians. Finding himself prisoner of these creatures, he escapes, only to encounter Woola and a princess in desperate need of a savior.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="John Carter", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    