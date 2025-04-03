
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Siege of Jadotville to the database
movies.insert(
    title="The Siege of Jadotville", 
    year=2016, 
    plot="Irish Commandant Pat Quinlan leads a stand off with troops against French and Belgian Mercenaries in the Congo during the early 1960s.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Siege of Jadotville", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    