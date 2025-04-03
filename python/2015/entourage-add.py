
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Entourage to the database
movies.insert(
    title="Entourage", 
    year=2015, 
    plot="Movie star Vincent Chase, together with his boys Eric, Turtle, and Johnny, are back - and back in business with super agent-turned-studio head Ari Gold on a risky project that will serve as Vince's directorial debut.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Entourage", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    