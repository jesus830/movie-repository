
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Limitless to the database
movies.insert(
    title="Limitless", 
    year=2011, 
    plot="With the help of a mysterious pill that enables the user to access 100 percent of his brain abilities, a struggling writer becomes a financial wizard, but it also puts him in a new world with lots of dangers.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Limitless", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    