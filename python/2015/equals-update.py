
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Equals", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Equals", 
        year=2015, 
        plot="In an emotionless utopia, two people fall in love when they regain their feelings from a mysterious disease, causing tensions between them and their society.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    