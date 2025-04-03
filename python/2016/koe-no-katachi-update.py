
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Koe no katachi", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Koe no katachi", 
        year=2016, 
        plot="The story revolves around Nishimiya Shoko, a grade school student who has impaired hearing. She transfers into a new school, where she is bullied by her classmates, especially Ishida Shouya... See full summary »", 
        rating=8.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    