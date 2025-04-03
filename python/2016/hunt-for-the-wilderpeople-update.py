
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hunt for the Wilderpeople", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hunt for the Wilderpeople", 
        year=2016, 
        plot="A national manhunt is ordered for a rebellious kid and his foster uncle who go missing in the wild New Zealand bush.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    