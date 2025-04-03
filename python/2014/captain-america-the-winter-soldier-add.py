
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Captain America: The Winter Soldier to the database
movies.insert(
    title="Captain America: The Winter Soldier", 
    year=2014, 
    plot="As Steve Rogers struggles to embrace his role in the modern world, he teams up with a fellow Avenger and S.H.I.E.L.D agent, Black Widow, to battle a new threat from history: an assassin known as the Winter Soldier.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Captain America: The Winter Soldier", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    