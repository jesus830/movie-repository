
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="True Crimes", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="True Crimes", 
        year=2016, 
        plot="A murder investigation of a slain business man turns to clues found in an author's book about an eerily similar crime. Based on the 2008 article "True Crimes - A postmodern murder mystery" by David Grann.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    