
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Forushande to the database
movies.insert(
    title="Forushande", 
    year=2016, 
    plot="While both participating in a production of "Death of a Salesman," a teacher's wife is assaulted in her new home, which leaves him determined to find the perpetrator over his wife's traumatized objections.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Forushande", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    