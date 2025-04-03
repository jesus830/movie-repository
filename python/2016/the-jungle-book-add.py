
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Jungle Book to the database
movies.insert(
    title="The Jungle Book", 
    year=2016, 
    plot="After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named Mowgli embarks on a journey of self discovery with the help of panther, Bagheera, and free spirited bear, Baloo.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Jungle Book", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    