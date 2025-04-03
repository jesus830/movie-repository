
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Three Musketeers to the database
movies.insert(
    title="The Three Musketeers", 
    year=2011, 
    plot="The hot-headed young D'Artagnan along with three former legendary but now down on their luck Musketeers must unite and defeat a beautiful double agent and her villainous employer from seizing the French throne and engulfing Europe in war.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Three Musketeers", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    