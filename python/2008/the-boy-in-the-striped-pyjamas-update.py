
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Boy in the Striped Pyjamas", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Boy in the Striped Pyjamas", 
        year=2008, 
        plot="Set during WWII, a story seen through the innocent eyes of Bruno, the eight-year-old son of the commandant at a German concentration camp, whose forbidden friendship with a Jewish boy on the other side of the camp fence has startling and unexpected consequences.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    