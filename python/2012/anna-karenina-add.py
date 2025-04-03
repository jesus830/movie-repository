
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Anna Karenina to the database
movies.insert(
    title="Anna Karenina", 
    year=2012, 
    plot="In late-19th-century Russian high society, St. Petersburg aristocrat Anna Karenina enters into a life-changing affair with the dashing Count Alexei Vronsky.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Anna Karenina", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    