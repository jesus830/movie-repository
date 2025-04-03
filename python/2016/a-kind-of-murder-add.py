
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Kind of Murder to the database
movies.insert(
    title="A Kind of Murder", 
    year=2016, 
    plot="In 1960s New York, Walter Stackhouse is a successful architect married to the beautiful Clara who leads a seemingly perfect life. But his fascination with an unsolved murder leads him into a spiral of chaos as he is forced to play cat-and-mouse with a clever killer and an overambitious detective, while at the same time lusting after another woman.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="A Kind of Murder", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    