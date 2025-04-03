
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Intent to the database
movies.insert(
    title="The Intent", 
    year=2016, 
    plot="Gunz (Dylan Duffus) is thrust into a world of excitement when he joins the TIC crew. The crew, led by the ruthless Hoodz (Scorcher), goes from low level weed peddling to full on armed ... See full summary »", 
    rating=3.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Intent", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    