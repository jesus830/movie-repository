
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mindhorn to the database
movies.insert(
    title="Mindhorn", 
    year=2016, 
    plot="A has-been actor best known for playing the title character in the 1980s detective series "Mindhorn" must work with the police when a serial killer says that he will only speak with Detective Mindhorn, whom he believes to be a real person.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Mindhorn", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    