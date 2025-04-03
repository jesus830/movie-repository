
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gone Girl to the database
movies.insert(
    title="Gone Girl", 
    year=2014, 
    plot="With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Gone Girl", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    