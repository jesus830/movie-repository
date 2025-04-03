
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Street Cat Named Bob", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Street Cat Named Bob", 
        year=2016, 
        plot="Based on the international best selling book. The true feel good story of how James Bowen, a busker and recovering drug addict, had his life transformed when he met a stray ginger cat.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    