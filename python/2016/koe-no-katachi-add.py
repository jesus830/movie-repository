
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Koe no katachi to the database
movies.insert(
    title="Koe no katachi", 
    year=2016, 
    plot="The story revolves around Nishimiya Shoko, a grade school student who has impaired hearing. She transfers into a new school, where she is bullied by her classmates, especially Ishida Shouya... See full summary »", 
    rating=8.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Koe no katachi", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    