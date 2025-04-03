
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Siege of Jadotville", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Siege of Jadotville", 
        year=2016, 
        plot="Irish Commandant Pat Quinlan leads a stand off with troops against French and Belgian Mercenaries in the Congo during the early 1960s.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    