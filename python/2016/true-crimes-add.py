
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add True Crimes to the database
movies.insert(
    title="True Crimes", 
    year=2016, 
    plot="A murder investigation of a slain business man turns to clues found in an author's book about an eerily similar crime. Based on the 2008 article "True Crimes - A postmodern murder mystery" by David Grann.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="True Crimes", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    