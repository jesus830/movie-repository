
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Survivalist to the database
movies.insert(
    title="The Survivalist", 
    year=2015, 
    plot="In a time of starvation, a survivalist lives off a small plot of land hidden deep in forest. When two women seeking food and shelter discover his farm, he finds his existence threatened.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Survivalist", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    