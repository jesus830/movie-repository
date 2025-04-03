
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Warrior to the database
movies.insert(
    title="Warrior", 
    year=2011, 
    plot="The youngest son of an alcoholic former boxer returns home, where he's trained by his father for competition in a mixed martial arts tournament - a path that puts the fighter on a collision course with his estranged, older brother.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Warrior", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    