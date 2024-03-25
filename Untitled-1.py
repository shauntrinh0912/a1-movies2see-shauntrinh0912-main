"""
Name: Trinh Xuan Son
Date started: 11/03/2024
GitHub URL (of this assignment):
Remember to NEVER make this assignment repo public
"""

import random
from operator import itemgetter
MENUS = """Menu:
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit"""

def main():
    print("Travel Tracker 1.0 - by Trinh Xuan Son")
    movie_list = read_file()
    print(f"{len(movie_list)} movies loaded from movies.csv")
    print(MENUS)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            display_choice(movie_list)
        elif choice == 'A':
            add_choice(movie_list)
        elif choice == 'W':
            watch_choice(movie_list)
        else:
            print("Invalid option")
        print(MENUS)
        choice = input(">>> ").upper()
    print(f"{len(movie_list)} movies saved to movies.csv")
    print("Have a nice day :)")



"""function to display details of movies"""

def display_choice(movie_list):
    movie_list = sorted(movie_list, key=itemgetter(2))
    movie_list = sorted(movie_list, key=itemgetter(1), reverse=True)
    # unwatched_movie mean movie have not watch
    unwatched_movie = 0
    # watched_movie mean movie already watched
    watched_movie = 0
    for index, movie in enumerate(movie_list):
        if movie[3] == 'u':
            unwatched_movie += 1
            print(f"{index + 1}.   {movie[0]:35} - {movie[1]:5} ({movie[2]})")
        elif movie[3] == 'w':
            watched_movie += 1
            print(f"{index + 1}. * {movie[0]:35} - {movie[1]:5} ({movie[2]})")



"""function to add new movie"""

def add_choice(movie_list):
    # this is default condition of new movie
    requirement = 'u'
    title = validate_input("Title: ").title()
    movie_year = validate_number("Year: ")
    category = validate_input("Category: ").title()
    new_movie = [title, str(movie_year), category, requirement]
    movie_list.append(new_movie)
    print(f"{title}  ({category} from {movie_year}) added to movie list.")



"""function to mark watched movie"""

def watch_choice(movie_list):
    # print movie details
    watched_movie = display_choice (movie_list)
    if watched_movie != len(movie_list):
        if watched_movie != len(movie_list):
            print("Enter the number of a movie to mark as watched")
            number = validate_number(">>> ")
            # check if number bigger than number of movie
            while number > len(movie_list):
                print("Invalid movie number")
                number = validate_number(">>> ")
            if movie_list[number - 1][-1] == 'w':
                print(f"You have already watched {movie_list[number - 1][0]}")
            else:
                movie_list[number - 1][-1] = 'w'
                print(f"{movie_list[number - 1][0]} from {movie_list[number - 1][1]} watched!")
        else:
            print("No more movies to watch !")



"""function to validate string input"""

def validate_input(message):
    user_input = input(message)
    is_correct = False
    while not is_correct:
        if user_input == '':
            print("Input can not be blank")
            user_input = input(message)
        else:
            is_correct = True
    return user_input



"""function to validate number"""

def validate_number(message):
    is_correct = False
    while not is_correct:
        try:
            movie_year = int(input(message))
            if movie_year > 0:
                is_correct = True
                return movie_year
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input, enter a valid number.")




"""function to read the file"""
def read_file():
    movie_list = []
    file = open('movies.csv', 'r')
    for line in file:
        # split the data by comma
        parts = line.strip().split(',')
        movie_list.append(parts)
    return movie_list


if __name__ == '__main__':
    main()
