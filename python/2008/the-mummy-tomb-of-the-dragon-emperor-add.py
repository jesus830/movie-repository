
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Mummy: Tomb of the Dragon Emperor to the database
movies.insert(
    title="The Mummy: Tomb of the Dragon Emperor", 
    year=2008, 
    plot="In the Far East, Alex O'Connell, the son of famed mummy fighters Rick and Evy O'Connell, unearths the mummy of the first Emperor of Qin -- a shape-shifting entity cursed by a witch centuries ago.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Mummy: Tomb of the Dragon Emperor", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    