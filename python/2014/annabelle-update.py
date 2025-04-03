
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Annabelle", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Annabelle", 
        year=2014, 
        plot="A couple begins to experience terrifying supernatural occurrences involving a vintage doll shortly after their home is invaded by satanic cultists.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    