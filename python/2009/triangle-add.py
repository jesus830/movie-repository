
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Triangle to the database
movies.insert(
    title="Triangle", 
    year=2009, 
    plot="The story revolves around the passengers of a yachting trip in the Atlantic Ocean who, when struck by mysterious weather conditions, jump to another ship only to experience greater havoc on the open seas.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Triangle", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    