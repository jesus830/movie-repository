
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Terminator Genisys to the database
movies.insert(
    title="Terminator Genisys", 
    year=2015, 
    plot="When John Connor, leader of the human resistance, sends Sgt. Kyle Reese back to 1984 to protect Sarah Connor and safeguard the future, an unexpected turn of events creates a fractured timeline.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Terminator Genisys", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    