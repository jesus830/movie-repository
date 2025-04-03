
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zero Dark Thirty to the database
movies.insert(
    title="Zero Dark Thirty", 
    year=2012, 
    plot="A chronicle of the decade-long hunt for al-Qaeda terrorist leader Osama bin Laden after the September 2001 attacks, and his death at the hands of the Navy S.E.A.L.s Team 6 in May 2011.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Zero Dark Thirty", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    