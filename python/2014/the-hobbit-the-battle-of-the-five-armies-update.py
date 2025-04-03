
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hobbit: The Battle of the Five Armies", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hobbit: The Battle of the Five Armies", 
        year=2014, 
        plot="Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    