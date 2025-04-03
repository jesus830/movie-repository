
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Mummy: Tomb of the Dragon Emperor", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Mummy: Tomb of the Dragon Emperor", 
        year=2008, 
        plot="In the Far East, Alex O'Connell, the son of famed mummy fighters Rick and Evy O'Connell, unearths the mummy of the first Emperor of Qin -- a shape-shifting entity cursed by a witch centuries ago.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    