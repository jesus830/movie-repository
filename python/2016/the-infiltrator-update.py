
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Infiltrator", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Infiltrator", 
        year=2016, 
        plot="A U.S. Customs official uncovers a money laundering scheme involving Colombian drug lord Pablo Escobar.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    