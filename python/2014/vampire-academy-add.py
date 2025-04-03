
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Vampire Academy to the database
movies.insert(
    title="Vampire Academy", 
    year=2014, 
    plot="Rose Hathaway is a Dhampir, half human-half vampire, a guardian of the Moroi, peaceful, mortal vampires living discreetly within our world. Her calling is to protect the Moroi from bloodthirsty, immortal Vampires, the Strigoi.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Vampire Academy", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    