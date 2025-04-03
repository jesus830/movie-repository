
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hobbit: The Desolation of Smaug to the database
movies.insert(
    title="The Hobbit: The Desolation of Smaug", 
    year=2013, 
    plot="The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hobbit: The Desolation of Smaug", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    