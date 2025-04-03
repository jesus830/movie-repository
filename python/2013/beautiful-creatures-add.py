
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Beautiful Creatures to the database
movies.insert(
    title="Beautiful Creatures", 
    year=2013, 
    plot="Ethan longs to escape his small Southern town. He meets a mysterious new girl, Lena. Together, they uncover dark secrets about their respective families, their history and their town.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Beautiful Creatures", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    