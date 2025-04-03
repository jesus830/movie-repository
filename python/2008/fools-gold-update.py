
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fool's Gold", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fool's Gold", 
        year=2008, 
        plot="A new clue to the whereabouts of a lost treasure rekindles a married couple's sense of adventure -- and their estranged romance.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    