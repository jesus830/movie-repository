
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Chef", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Chef", 
        year=2014, 
        plot="A head chef quits his restaurant job and buys a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    