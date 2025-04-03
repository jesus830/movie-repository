
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Folk Hero & Funny Guy to the database
movies.insert(
    title="Folk Hero & Funny Guy", 
    year=2016, 
    plot="A successful singer-songwriter hatches a plan to help his friend's struggling comedy career and broken love life by hiring him as his opening act on his solo tour.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Folk Hero & Funny Guy", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    