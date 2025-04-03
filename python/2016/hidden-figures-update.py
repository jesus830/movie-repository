
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hidden Figures", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hidden Figures", 
        year=2016, 
        plot="The story of a team of female African-American mathematicians who served a vital role in NASA during the early years of the U.S. space program.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    