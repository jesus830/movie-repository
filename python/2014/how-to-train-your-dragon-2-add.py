
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add How to Train Your Dragon 2 to the database
movies.insert(
    title="How to Train Your Dragon 2", 
    year=2014, 
    plot="When Hiccup and Toothless discover an ice cave that is home to hundreds of new wild dragons and the mysterious Dragon Rider, the two friends find themselves at the center of a battle to protect the peace.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="How to Train Your Dragon 2", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    