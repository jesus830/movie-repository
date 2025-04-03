
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Unknown", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Unknown", 
        year=2011, 
        plot="A man awakens from a coma, only to discover that someone has taken on his identity and that no one, (not even his wife), believes him. With the help of a young woman, he sets out to prove who he is.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    