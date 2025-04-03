
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sleeping with Other People to the database
movies.insert(
    title="Sleeping with Other People", 
    year=2015, 
    plot="A good-natured womanizer and a serial cheater form a platonic relationship that helps reform them in ways, while a mutual attraction sets in.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Sleeping with Other People", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    