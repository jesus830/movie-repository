
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Filth to the database
movies.insert(
    title="Filth", 
    year=2013, 
    plot="A corrupt, junkie cop with bipolar disorder attempts to manipulate his way through a promotion in order to win back his wife and daughter while also fighting his own borderline-fueled inner demons.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Filth", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    