
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Despicable Me 2 to the database
movies.insert(
    title="Despicable Me 2", 
    year=2013, 
    plot="When Gru, the world's most super-bad turned super-dad has been recruited by a team of officials to stop lethal muscle and a host of Gru's own, He has to fight back with new gadgetry, cars, and more minion madness.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Despicable Me 2", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    