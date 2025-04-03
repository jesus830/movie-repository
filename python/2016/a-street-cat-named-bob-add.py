
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Street Cat Named Bob to the database
movies.insert(
    title="A Street Cat Named Bob", 
    year=2016, 
    plot="Based on the international best selling book. The true feel good story of how James Bowen, a busker and recovering drug addict, had his life transformed when he met a stray ginger cat.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="A Street Cat Named Bob", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    