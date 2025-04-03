
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mr. Church to the database
movies.insert(
    title="Mr. Church", 
    year=2016, 
    plot=""Mr. Church" tells the story of a unique friendship that develops when a little girl and her dying mother retain the services of a talented cook - Henry Joseph Church. What begins as a six month arrangement instead spans into fifteen years and creates a family bond that lasts forever.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Church", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    