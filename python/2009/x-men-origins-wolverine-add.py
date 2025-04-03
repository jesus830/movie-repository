
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add X-Men Origins: Wolverine to the database
movies.insert(
    title="X-Men Origins: Wolverine", 
    year=2009, 
    plot="A look at Wolverine's early life, in particular his time with the government squad Team X and the impact it will have on his later years.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="X-Men Origins: Wolverine", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    