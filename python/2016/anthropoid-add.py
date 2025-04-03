
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Anthropoid to the database
movies.insert(
    title="Anthropoid", 
    year=2016, 
    plot="Based on the extraordinary true story of Operation Anthropoid, the WWII mission to assassinate SS General Reinhard Heydrich, the main architect behind the Final Solution and the Reich's third in command after Hitler and Himmler.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Anthropoid", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    