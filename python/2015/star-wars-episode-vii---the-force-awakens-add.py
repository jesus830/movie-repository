
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Star Wars: Episode VII - The Force Awakens to the database
movies.insert(
    title="Star Wars: Episode VII - The Force Awakens", 
    year=2015, 
    plot="Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Star Wars: Episode VII - The Force Awakens", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    