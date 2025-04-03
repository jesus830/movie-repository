
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mike and Dave Need Wedding Dates to the database
movies.insert(
    title="Mike and Dave Need Wedding Dates", 
    year=2016, 
    plot="Two hard-partying brothers place an online ad to find the perfect dates for their sister's Hawaiian wedding. Hoping for a wild getaway, the boys instead find themselves out-hustled by an uncontrollable duo.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Mike and Dave Need Wedding Dates", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    