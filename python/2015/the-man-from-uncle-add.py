
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Man from U.N.C.L.E. to the database
movies.insert(
    title="The Man from U.N.C.L.E.", 
    year=2015, 
    plot="In the early 1960s, CIA agent Napoleon Solo and KGB operative Illya Kuryakin participate in a joint mission against a mysterious criminal organization, which is working to proliferate nuclear weapons.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Man from U.N.C.L.E.", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    