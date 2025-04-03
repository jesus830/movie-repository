
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Huntsman: Winter's War", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Huntsman: Winter's War", 
        year=2016, 
        plot="Eric and fellow warrior Sara, raised as members of ice Queen Freya's army, try to conceal their forbidden love as they fight to survive the wicked intentions of both Freya and her sister Ravenna.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    