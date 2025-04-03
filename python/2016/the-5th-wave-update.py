
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The 5th Wave", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The 5th Wave", 
        year=2016, 
        plot="Four waves of increasingly deadly alien attacks have left most of Earth decimated. Cassie is on the run, desperately trying to save her younger brother.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    