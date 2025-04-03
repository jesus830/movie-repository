
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Sniper to the database
movies.insert(
    title="American Sniper", 
    year=2014, 
    plot="Navy S.E.A.L. sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="American Sniper", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    