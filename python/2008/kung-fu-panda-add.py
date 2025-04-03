
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kung Fu Panda to the database
movies.insert(
    title="Kung Fu Panda", 
    year=2008, 
    plot="The Dragon Warrior has to clash against the savage Tai Lung as China's fate hangs in the balance: However, the Dragon Warrior mantle is supposedly mistaken to be bestowed upon an obese panda who is a tyro in martial arts.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Kung Fu Panda", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    