
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Exodus: Gods and Kings to the database
movies.insert(
    title="Exodus: Gods and Kings", 
    year=2014, 
    plot="The defiant leader Moses rises up against the Egyptian Pharaoh Ramses, setting 600,000 slaves on a monumental journey of escape from Egypt and its terrifying cycle of deadly plagues.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Exodus: Gods and Kings", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    