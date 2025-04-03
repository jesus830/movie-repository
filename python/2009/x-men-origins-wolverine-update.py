
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="X-Men Origins: Wolverine", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="X-Men Origins: Wolverine", 
        year=2009, 
        plot="A look at Wolverine's early life, in particular his time with the government squad Team X and the impact it will have on his later years.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    