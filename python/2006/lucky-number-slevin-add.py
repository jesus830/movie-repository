
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lucky Number Slevin to the database
movies.insert(
    title="Lucky Number Slevin", 
    year=2006, 
    plot="A case of mistaken identity lands Slevin into the middle of a war being plotted by two of the city's most rival crime bosses: The Rabbi and The Boss. Slevin is under constant surveillance by relentless Detective Brikowski as well as the infamous assassin Goodkat and finds himself having to hatch his own ingenious plot to get them before they get him.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Lucky Number Slevin", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    