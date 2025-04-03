
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Survivalist", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Survivalist", 
        year=2015, 
        plot="In a time of starvation, a survivalist lives off a small plot of land hidden deep in forest. When two women seeking food and shelter discover his farm, he finds his existence threatened.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    