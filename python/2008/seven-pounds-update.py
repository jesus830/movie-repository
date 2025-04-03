
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Seven Pounds", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Seven Pounds", 
        year=2008, 
        plot="A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    