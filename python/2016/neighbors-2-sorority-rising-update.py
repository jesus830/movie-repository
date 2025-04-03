
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Neighbors 2: Sorority Rising", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Neighbors 2: Sorority Rising", 
        year=2016, 
        plot="When their new next-door neighbors turn out to be a sorority even more debaucherous than the fraternity previously living there, Mac and Kelly team with their former enemy, Teddy, to bring the girls down.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    