
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bridge of Spies to the database
movies.insert(
    title="Bridge of Spies", 
    year=2015, 
    plot="During the Cold War, an American lawyer is recruited to defend an arrested Soviet spy in court, and then help the CIA facilitate an exchange of the spy for the Soviet captured American U2 spy plane pilot, Francis Gary Powers.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Bridge of Spies", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    