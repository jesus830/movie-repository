
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fantastic Beasts and Where to Find Them", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fantastic Beasts and Where to Find Them", 
        year=2016, 
        plot="The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    