
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Talladega Nights: The Ballad of Ricky Bobby to the database
movies.insert(
    title="Talladega Nights: The Ballad of Ricky Bobby", 
    year=2006, 
    plot="#1 NASCAR driver Ricky Bobby stays atop the heap thanks to a pact with his best friend and teammate, Cal Naughton, Jr. But when a French Formula One driver, makes his way up the ladder, Ricky Bobby's talent and devotion are put to the test.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Talladega Nights: The Ballad of Ricky Bobby", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    