
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Last Face to the database
movies.insert(
    title="The Last Face", 
    year=2016, 
    plot="A director (Charlize Theron) of an international aid agency in Africa meets a relief aid doctor (Javier Bardem) amidst a political/social revolution, and together face tough choices ... See full summary »", 
    rating=3.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Last Face", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    