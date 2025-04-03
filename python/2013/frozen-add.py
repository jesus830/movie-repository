
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Frozen to the database
movies.insert(
    title="Frozen", 
    year=2013, 
    plot="When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Frozen", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    