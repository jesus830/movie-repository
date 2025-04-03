
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Town to the database
movies.insert(
    title="The Town", 
    year=2010, 
    plot="As he plans his next job, a longtime thief tries to balance his feelings for a bank manager connected to one of his earlier heists, as well as the FBI agent looking to bring him and his crew down.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Town", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    