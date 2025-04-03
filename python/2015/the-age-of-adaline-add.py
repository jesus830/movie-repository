
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Age of Adaline to the database
movies.insert(
    title="The Age of Adaline", 
    year=2015, 
    plot="A young woman, born at the turn of the 20th century, is rendered ageless after an accident. After many solitary years, she meets a man who complicates the eternal life she has settled into.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Age of Adaline", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    