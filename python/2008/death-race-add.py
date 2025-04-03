
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Death Race to the database
movies.insert(
    title="Death Race", 
    year=2008, 
    plot="Ex-con Jensen Ames is forced by the warden of a notorious prison to compete in our post-industrial world's most popular sport: a car race in which inmates must brutalize and kill one another on the road to victory.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Death Race", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    