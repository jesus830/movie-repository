
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Megamind to the database
movies.insert(
    title="Megamind", 
    year=2010, 
    plot="The supervillain Megamind finally defeats his nemesis, the superhero Metro Man. But without a hero, he loses all purpose and must find new meaning to his life.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Megamind", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    