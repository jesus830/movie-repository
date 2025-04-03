
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Girl with All the Gifts", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Girl with All the Gifts", 
        year=2016, 
        plot="A scientist and a teacher living in a dystopian future embark on a journey of survival with a special young girl named Melanie.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    