
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Imaginarium of Doctor Parnassus to the database
movies.insert(
    title="The Imaginarium of Doctor Parnassus", 
    year=2009, 
    plot="A traveling theater company gives its audience much more than they were expecting.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Imaginarium of Doctor Parnassus", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    