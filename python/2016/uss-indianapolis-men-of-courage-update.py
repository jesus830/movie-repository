
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="USS Indianapolis: Men of Courage", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="USS Indianapolis: Men of Courage", 
        year=2016, 
        plot="During World War II, an American navy ship is sunk by a Japanese submarine leaving 300 crewmen stranded in shark infested waters.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    