
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Avengers: Age of Ultron to the database
movies.insert(
    title="Avengers: Age of Ultron", 
    year=2015, 
    plot="When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's mightiest heroes to stop the villainous Ultron from enacting his terrible plan.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Avengers: Age of Ultron", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    