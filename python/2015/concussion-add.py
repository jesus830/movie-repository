
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Concussion to the database
movies.insert(
    title="Concussion", 
    year=2015, 
    plot="In Pittsburgh, accomplished pathologist Dr. Bennet Omalu uncovers the truth about brain damage in football players who suffer repeated concussions in the course of normal play.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Concussion", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    