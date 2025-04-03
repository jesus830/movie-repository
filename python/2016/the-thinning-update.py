
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Thinning", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Thinning", 
        year=2016, 
        plot=""The Thinning" takes place in a post-apocalyptic future where population control is dictated by a high-school aptitude test. When two students (Logan Paul and Peyton List) discover the test... See full summary »", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    