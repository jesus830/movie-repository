
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sex and the City to the database
movies.insert(
    title="Sex and the City", 
    year=2008, 
    plot="A New York writer on sex and love is finally getting married to her Mr. Big. But her three best girlfriends must console her after one of them inadvertently leads Mr. Big to jilt her.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Sex and the City", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    