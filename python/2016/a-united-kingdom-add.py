
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A United Kingdom to the database
movies.insert(
    title="A United Kingdom", 
    year=2016, 
    plot="The story of King Seretse Khama of Botswana and how his loving but controversial marriage to a British white woman, Ruth Williams, put his kingdom into political and diplomatic turmoil.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="A United Kingdom", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    