
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Wrestler: The Wizard to the database
movies.insert(
    title="American Wrestler: The Wizard", 
    year=2016, 
    plot="In 1980, a teenage boy escapes the unrest in Iran only to face more hostility in America, due to the hostage crisis. Determined to fit in, he joins the school's floundering wrestling team.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="American Wrestler: The Wizard", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    