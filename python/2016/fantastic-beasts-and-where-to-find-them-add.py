
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fantastic Beasts and Where to Find Them to the database
movies.insert(
    title="Fantastic Beasts and Where to Find Them", 
    year=2016, 
    plot="The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Fantastic Beasts and Where to Find Them", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    