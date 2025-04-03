
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Kind of Murder", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Kind of Murder", 
        year=2016, 
        plot="In 1960s New York, Walter Stackhouse is a successful architect married to the beautiful Clara who leads a seemingly perfect life. But his fascination with an unsolved murder leads him into a spiral of chaos as he is forced to play cat-and-mouse with a clever killer and an overambitious detective, while at the same time lusting after another woman.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    