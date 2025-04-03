
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="En man som heter Ove", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="En man som heter Ove", 
        year=2015, 
        plot="Ove, an ill-tempered, isolated retiree who spends his days enforcing block association rules and visiting his wife's grave, has finally given up on life just as an unlikely friendship develops with his boisterous new neighbors.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    