
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pompeii to the database
movies.insert(
    title="Pompeii", 
    year=2014, 
    plot="A slave-turned-gladiator finds himself in a race against time to save his true love, who has been betrothed to a corrupt Roman Senator. As Mount Vesuvius erupts, he must fight to save his beloved as Pompeii crumbles around him.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Pompeii", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    