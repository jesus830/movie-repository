
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Into the Wild to the database
movies.insert(
    title="Into the Wild", 
    year=2007, 
    plot="After graduating from Emory University, top student and athlete Christopher McCandless abandons his possessions, gives his entire $24,000 savings account to charity and hitchhikes to Alaska to live in the wilderness. Along the way, Christopher encounters a series of characters that shape his life.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Into the Wild", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    