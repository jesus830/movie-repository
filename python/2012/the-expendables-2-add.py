
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Expendables 2 to the database
movies.insert(
    title="The Expendables 2", 
    year=2012, 
    plot="Mr. Church reunites the Expendables for what should be an easy paycheck, but when one of their men is murdered on the job, their quest for revenge puts them deep in enemy territory and up against an unexpected threat.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Expendables 2", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    