
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Into the Woods to the database
movies.insert(
    title="Into the Woods", 
    year=2014, 
    plot="A witch tasks a childless baker and his wife with procuring magical items from classic fairy tales to reverse the curse put on their family tree.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Into the Woods", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    