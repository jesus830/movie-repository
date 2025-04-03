
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hidden Figures to the database
movies.insert(
    title="Hidden Figures", 
    year=2016, 
    plot="The story of a team of female African-American mathematicians who served a vital role in NASA during the early years of the U.S. space program.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Hidden Figures", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    