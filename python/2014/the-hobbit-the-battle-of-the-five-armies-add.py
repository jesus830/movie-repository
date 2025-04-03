
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hobbit: The Battle of the Five Armies to the database
movies.insert(
    title="The Hobbit: The Battle of the Five Armies", 
    year=2014, 
    plot="Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hobbit: The Battle of the Five Armies", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    