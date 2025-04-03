
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Equalizer to the database
movies.insert(
    title="The Equalizer", 
    year=2014, 
    plot="A man believes he has put his mysterious past behind him and has dedicated himself to beginning a new, quiet life. But when he meets a young girl under the control of ultra-violent Russian gangsters, he can't stand idly by - he has to help her.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Equalizer", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    