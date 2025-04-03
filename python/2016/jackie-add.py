
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jackie to the database
movies.insert(
    title="Jackie", 
    year=2016, 
    plot="Following the assassination of President John F. Kennedy, First Lady Jacqueline Kennedy fights through grief and trauma to regain her faith, console her children, and define her husband's historic legacy.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Jackie", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    