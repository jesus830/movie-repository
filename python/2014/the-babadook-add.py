
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Babadook to the database
movies.insert(
    title="The Babadook", 
    year=2014, 
    plot="A single mother, plagued by the violent death of her husband, battles with her son's fear of a monster lurking in the house, but soon discovers a sinister presence all around her.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Babadook", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    