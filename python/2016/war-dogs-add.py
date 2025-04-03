
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add War Dogs to the database
movies.insert(
    title="War Dogs", 
    year=2016, 
    plot="Based on the true story of two young men, David Packouz and Efraim Diveroli, who won a $300 million contract from the Pentagon to arm America's allies in Afghanistan.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="War Dogs", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    