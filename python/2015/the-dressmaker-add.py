
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Dressmaker to the database
movies.insert(
    title="The Dressmaker", 
    year=2015, 
    plot="A glamorous woman returns to her small town in rural Australia. With her sewing machine and haute couture style, she transforms the women and exacts sweet revenge on those who did her wrong.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Dressmaker", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    