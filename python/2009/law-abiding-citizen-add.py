
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Law Abiding Citizen to the database
movies.insert(
    title="Law Abiding Citizen", 
    year=2009, 
    plot="A frustrated man decides to take justice into his own hands after a plea bargain sets one of his family's killers free. He targets not only the killer but also the district attorney and others involved in the deal.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Law Abiding Citizen", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    