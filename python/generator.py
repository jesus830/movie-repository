import boto3
import csv

s3 = boto3.resource('s3')

def add_movie(id, title, year, plot, rating):
    file = f'''
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add {title} to the database
movies.insert(
    title="{title}", 
    year={year}, 
    plot="{plot}", 
    rating={rating}
)

# Confirm that the movie was added
movie = movies.select(
    title="{title}", 
    year={year}
)
if movie:
    # The movie was found
    print(f"Movie found: {{movie}}")
else:
    # The movie was not found
    print("Movie not found")
    '''

    # put the file contents to s3 object
    object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/python/{year}/{id}-add.py')
    object.put(Body=file.encode('utf-8'))


def delete_movie(id, title, year, plot, rating):
    file = f'''
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie exists in the database
movie = movies.select(
    title="{title}", 
    year={year}
)

if movie:
    # Delete the movie
    print("Deleting movie")
    movies.delete(
        title="{title}", 
        year={year}
    )
else:
    # Warn that the movie doesn't exist
    print("Movie not found; therefore, no need to delete it.")
    '''

    # put the file contents to s3 object
    object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/python/{year}/{id}-delete.py')
    object.put(Body=file.encode('utf-8'))


def get_movie(id, title, year, plot, rating):
    file = f'''
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="{title}", 
    year={year}
)

if movie:
    # The movie was found
    print("Movie found")
else:
    # The movie was not found
    print("Movie not found")
    '''

    # put the file contents to s3 object
    object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/python/{year}/{id}-get.py')
    object.put(Body=file.encode('utf-8'))


def update_movie(id, title, year, plot, rating):
    file = f'''
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="{title}", 
    year={year}
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="{title}", 
        year={year}, 
        plot="{plot}", 
        rating={rating}
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    '''

    # put the file contents to s3 object
    object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/python/{year}/{id}-update.py')
    object.put(Body=file.encode('utf-8'))



with open('movies.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)
    
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Access the columns in each row
        # id = row[0]
        title = row[1].replace("\"", "")
        id = ''.join(letter for letter in title.lower().replace(' ','-') if letter.isalnum() or letter == '-')
        plot = row[3]
        year = row[6]
        rating = row[8]

        add_movie(id, title, year, plot, rating)
        delete_movie(id, title, year, plot, rating)
        get_movie(id, title, year, plot, rating)
        update_movie(id, title, year, plot, rating)
        
        # Process the data as needed
        print(f"{year}/{id}")