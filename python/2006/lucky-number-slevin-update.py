
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Lucky Number Slevin", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Lucky Number Slevin", 
        year=2006, 
        plot="A case of mistaken identity lands Slevin into the middle of a war being plotted by two of the city's most rival crime bosses: The Rabbi and The Boss. Slevin is under constant surveillance by relentless Detective Brikowski as well as the infamous assassin Goodkat and finds himself having to hatch his own ingenious plot to get them before they get him.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    