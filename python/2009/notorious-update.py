
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Notorious", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Notorious", 
        year=2009, 
        plot="The life and death story of Notorious B.I.G. (a.k.a. Christopher Wallace), who came straight out of Brooklyn to take the world of rap music by storm.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    