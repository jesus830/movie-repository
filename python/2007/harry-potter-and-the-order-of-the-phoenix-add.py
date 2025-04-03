
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Harry Potter and the Order of the Phoenix to the database
movies.insert(
    title="Harry Potter and the Order of the Phoenix", 
    year=2007, 
    plot="With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Order of the Phoenix", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    