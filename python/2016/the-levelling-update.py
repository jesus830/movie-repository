
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Levelling", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Levelling", 
        year=2016, 
        plot="Somerset, October 2014. When Clover Catto (Ellie Kendrick) receives a call telling her that her younger brother Harry (Joe Blakemore) is dead, she must return to her family farm and face ... See full summary »", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    