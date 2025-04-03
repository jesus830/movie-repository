
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sex and the City 2 to the database
movies.insert(
    title="Sex and the City 2", 
    year=2010, 
    plot="While wrestling with the pressures of life, love, and work in Manhattan, Carrie, Miranda, and Charlotte join Samantha for a trip to Abu Dhabi (United Arab Emirates), where Samantha's ex is filming a new movie.", 
    rating=4.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Sex and the City 2", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    