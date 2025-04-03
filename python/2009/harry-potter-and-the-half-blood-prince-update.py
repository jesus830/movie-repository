
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Half-Blood Prince", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Harry Potter and the Half-Blood Prince", 
        year=2009, 
        plot="As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as "the property of the Half-Blood Prince" and begins to learn more about Lord Voldemort's dark past.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    