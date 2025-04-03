
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add We Need to Talk About Kevin to the database
movies.insert(
    title="We Need to Talk About Kevin", 
    year=2011, 
    plot="Kevin's mother struggles to love her strange child, despite the increasingly vicious things he says and does as he grows up. But Kevin is just getting started, and his final act will be beyond anything anyone imagined.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="We Need to Talk About Kevin", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    