
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Gone Girl", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Gone Girl", 
        year=2014, 
        plot="With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    