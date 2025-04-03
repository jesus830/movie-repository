
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Assassination of Jesse James by the Coward Robert Ford to the database
movies.insert(
    title="The Assassination of Jesse James by the Coward Robert Ford", 
    year=2007, 
    plot="Robert Ford, who's idolized Jesse James since childhood, tries hard to join the reforming gang of the Missouri outlaw, but gradually becomes resentful of the bandit leader.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Assassination of Jesse James by the Coward Robert Ford", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    