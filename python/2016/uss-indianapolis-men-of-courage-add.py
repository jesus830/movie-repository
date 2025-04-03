
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add USS Indianapolis: Men of Courage to the database
movies.insert(
    title="USS Indianapolis: Men of Courage", 
    year=2016, 
    plot="During World War II, an American navy ship is sunk by a Japanese submarine leaving 300 crewmen stranded in shark infested waters.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="USS Indianapolis: Men of Courage", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    