
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Forushande", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Forushande", 
        year=2016, 
        plot="While both participating in a production of "Death of a Salesman," a teacher's wife is assaulted in her new home, which leaves him determined to find the perpetrator over his wife's traumatized objections.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    