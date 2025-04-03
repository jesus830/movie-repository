
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bridesmaids to the database
movies.insert(
    title="Bridesmaids", 
    year=2011, 
    plot="Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Bridesmaids", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    