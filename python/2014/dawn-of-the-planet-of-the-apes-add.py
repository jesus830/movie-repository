
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dawn of the Planet of the Apes to the database
movies.insert(
    title="Dawn of the Planet of the Apes", 
    year=2014, 
    plot="A growing nation of genetically evolved apes led by Caesar is threatened by a band of human survivors of the devastating virus unleashed a decade earlier.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Dawn of the Planet of the Apes", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    