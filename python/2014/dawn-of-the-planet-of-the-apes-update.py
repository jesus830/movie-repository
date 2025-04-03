
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Dawn of the Planet of the Apes", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Dawn of the Planet of the Apes", 
        year=2014, 
        plot="A growing nation of genetically evolved apes led by Caesar is threatened by a band of human survivors of the devastating virus unleashed a decade earlier.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    