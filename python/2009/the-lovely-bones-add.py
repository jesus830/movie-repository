
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lovely Bones to the database
movies.insert(
    title="The Lovely Bones", 
    year=2009, 
    plot="Centers on a young girl who has been murdered and watches over her family - and her killer - from purgatory. She must weigh her desire for vengeance against her desire for her family to heal.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lovely Bones", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    