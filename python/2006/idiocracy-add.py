
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Idiocracy to the database
movies.insert(
    title="Idiocracy", 
    year=2006, 
    plot="Private Joe Bauers, the definition of "average American", is selected by the Pentagon to be the guinea pig for a top-secret hibernation program. Forgotten, he awakes five centuries in the future. He discovers a society so incredibly dumbed down that he's easily the most intelligent person alive.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Idiocracy", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    