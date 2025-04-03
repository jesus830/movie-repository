
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Les Misérables to the database
movies.insert(
    title="Les Misérables", 
    year=2012, 
    plot="In 19th-century France, Jean Valjean, who for decades has been hunted by the ruthless policeman Javert after breaking parole, agrees to care for a factory worker's daughter. The decision changes their lives forever.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Les Misérables", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    