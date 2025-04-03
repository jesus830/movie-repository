
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Taare Zameen Par", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Taare Zameen Par", 
        year=2007, 
        plot="An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.", 
        rating=8.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    