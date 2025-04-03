
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Unbroken to the database
movies.insert(
    title="Unbroken", 
    year=2014, 
    plot="After a near-fatal plane crash in WWII, Olympian Louis Zamperini spends a harrowing 47 days in a raft with two fellow crewmen before he's caught by the Japanese navy and sent to a prisoner-of-war camp.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Unbroken", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    