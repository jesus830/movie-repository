
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Internship to the database
movies.insert(
    title="The Internship", 
    year=2013, 
    plot="Two salesmen whose careers have been torpedoed by the digital age find their way into a coveted internship at Google, where they must compete with a group of young, tech-savvy geniuses for a shot at employment.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Internship", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    