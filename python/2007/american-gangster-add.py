
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Gangster to the database
movies.insert(
    title="American Gangster", 
    year=2007, 
    plot="In 1970s America, a detective works to bring down the drug empire of Frank Lucas, a heroin kingpin from Manhattan, who is smuggling the drug into the country from the Far East.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="American Gangster", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    