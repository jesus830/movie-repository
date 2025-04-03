
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Alexander and the Terrible, Horrible, No Good, Very Bad Day", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Alexander and the Terrible, Horrible, No Good, Very Bad Day", 
        year=2014, 
        plot="Alexander's day begins with gum stuck in his hair, followed by more calamities. However, he finds little sympathy from his family and begins to wonder if bad things only happen to him, his mom, dad, brother and sister - who all find themselves living through their own terrible, horrible, no good, very bad day.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    