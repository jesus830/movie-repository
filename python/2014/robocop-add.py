
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add RoboCop to the database
movies.insert(
    title="RoboCop", 
    year=2014, 
    plot="In 2028 Detroit, when Alex Murphy - a loving husband, father and good cop - is critically injured in the line of duty, the multinational conglomerate OmniCorp sees their chance for a part-man, part-robot police officer.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="RoboCop", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    