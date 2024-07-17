favorite_movies = []

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Added '{movie}' to movie list.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Removed '{movie}' from movie list.")
    else:
        print(f"'{movie}' movie not found.")

def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    num_movies = len(favorite_movies)
    print(f"There are {num_movies} movies in the list")

def find_movie(movie):
    if movie in favorite_movies:
        print(f"'{movie}' is in the movie list.")
    else:
        print(f"'{movie}' is not in the movie list.")

def clear_movies():
    favorite_movies.clear()
    print("All movies cleared from list")

add_movie("Batman")
add_movie("Batman Returns")
add_movie("Batman: Mask of the Phantasm")
add_movie("Batman Forever")
add_movie("Batman and Robin")

display_movies()

count_movies()
find_movie("Batman and Robin")
remove_movie("Batman and Robin")
find_movie("Batman and Robin")
remove_movie("Batgirl")

display_movies()
count_movies()

clear_movies()
count_movies()
display_movies()