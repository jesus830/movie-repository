
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Stakelander", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Stakelander", 
        year=2016, 
        plot="When his home of New Eden is destroyed by a revitalized Brotherhood and its new Vamp leader, Martin finds himself alone in the badlands of America with only the distant memory of his mentor and legendary vampire hunter, Mister, to guide him.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    