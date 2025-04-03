
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Folk Hero & Funny Guy", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Folk Hero & Funny Guy", 
        year=2016, 
        plot="A successful singer-songwriter hatches a plan to help his friend's struggling comedy career and broken love life by hiring him as his opening act on his solo tour.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    