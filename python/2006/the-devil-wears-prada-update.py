
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Devil Wears Prada", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Devil Wears Prada", 
        year=2006, 
        plot="A smart but sensible new graduate lands a job as an assistant to Miranda Priestly, the demanding editor-in-chief of a high fashion magazine.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    