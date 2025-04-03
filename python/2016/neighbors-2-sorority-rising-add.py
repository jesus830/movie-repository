
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Neighbors 2: Sorority Rising to the database
movies.insert(
    title="Neighbors 2: Sorority Rising", 
    year=2016, 
    plot="When their new next-door neighbors turn out to be a sorority even more debaucherous than the fraternity previously living there, Mac and Kelly team with their former enemy, Teddy, to bring the girls down.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Neighbors 2: Sorority Rising", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    