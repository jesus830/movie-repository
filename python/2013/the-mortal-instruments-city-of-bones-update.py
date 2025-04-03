
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Mortal Instruments: City of Bones", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Mortal Instruments: City of Bones", 
        year=2013, 
        plot="When her mother disappears, Clary Fray learns that she descends from a line of warriors who protect our world from demons. She joins forces with others like her and heads into a dangerous alternate New York called the Shadow World.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    