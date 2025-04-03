
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="American Wrestler: The Wizard", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="American Wrestler: The Wizard", 
        year=2016, 
        plot="In 1980, a teenage boy escapes the unrest in Iran only to face more hostility in America, due to the hostage crisis. Determined to fit in, he joins the school's floundering wrestling team.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    