
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Alexander and the Terrible, Horrible, No Good, Very Bad Day to the database
movies.insert(
    title="Alexander and the Terrible, Horrible, No Good, Very Bad Day", 
    year=2014, 
    plot="Alexander's day begins with gum stuck in his hair, followed by more calamities. However, he finds little sympathy from his family and begins to wonder if bad things only happen to him, his mom, dad, brother and sister - who all find themselves living through their own terrible, horrible, no good, very bad day.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Alexander and the Terrible, Horrible, No Good, Very Bad Day", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    