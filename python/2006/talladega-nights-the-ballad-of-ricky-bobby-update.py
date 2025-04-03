
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Talladega Nights: The Ballad of Ricky Bobby", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Talladega Nights: The Ballad of Ricky Bobby", 
        year=2006, 
        plot="#1 NASCAR driver Ricky Bobby stays atop the heap thanks to a pact with his best friend and teammate, Cal Naughton, Jr. But when a French Formula One driver, makes his way up the ladder, Ricky Bobby's talent and devotion are put to the test.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    