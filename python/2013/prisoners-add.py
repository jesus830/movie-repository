
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Prisoners to the database
movies.insert(
    title="Prisoners", 
    year=2013, 
    plot="When Keller Dover's daughter and her friend go missing, he takes matters into his own hands as the police pursue multiple leads and the pressure mounts.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Prisoners", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    