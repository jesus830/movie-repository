
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Annie", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Annie", 
        year=2014, 
        plot="A foster kid, who lives with her mean foster mom, sees her life change when business tycoon and New York mayoral candidate Will Stacks makes a thinly-veiled campaign move and takes her in.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    