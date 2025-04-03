
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sweeney Todd: The Demon Barber of Fleet Street to the database
movies.insert(
    title="Sweeney Todd: The Demon Barber of Fleet Street", 
    year=2007, 
    plot="The infamous story of Benjamin Barker, a.k.a. Sweeney Todd, who sets up a barber shop down in London which is the basis for a sinister partnership with his fellow tenant, Mrs. Lovett. Based on the hit Broadway musical.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Sweeney Todd: The Demon Barber of Fleet Street", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    