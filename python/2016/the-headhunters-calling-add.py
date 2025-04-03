
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Headhunter's Calling to the database
movies.insert(
    title="The Headhunter's Calling", 
    year=2016, 
    plot="A headhunter whose life revolves around closing deals in a a survival-of-the-fittest boiler room, battles his top rival for control of their job placement company -- his dream of owning the company clashing with the needs of his family.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Headhunter's Calling", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    