
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Legion", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Legion", 
        year=2010, 
        plot="When a group of strangers at a dusty roadside diner come under attack by demonic forces, their only chance for survival lies with an archangel named Michael, who informs a pregnant waitress that her unborn child is humanity's last hope.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    