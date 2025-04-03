
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Blind Side to the database
movies.insert(
    title="The Blind Side", 
    year=2009, 
    plot="The story of Michael Oher, a homeless and traumatized boy who became an All American football player and first round NFL draft pick with the help of a caring woman and her family.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Blind Side", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    