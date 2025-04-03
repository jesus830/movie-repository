
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Exception to the database
movies.insert(
    title="The Exception", 
    year=2016, 
    plot="A German soldier tries to determine if the Dutch resistance has planted a spy to infiltrate the home of Kaiser Wilhelm in Holland during the onset of World War II, but falls for a young Jewish Dutch woman during his investigation.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Exception", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    