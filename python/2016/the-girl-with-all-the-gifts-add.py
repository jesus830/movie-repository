
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Girl with All the Gifts to the database
movies.insert(
    title="The Girl with All the Gifts", 
    year=2016, 
    plot="A scientist and a teacher living in a dystopian future embark on a journey of survival with a special young girl named Melanie.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Girl with All the Gifts", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    