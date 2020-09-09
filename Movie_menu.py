#! /usr/bin/python3

movies = []


def menu():
    user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown Command!')
        user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the director  name: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies():
    if movies:
        for movie in movies:
            print(movie['name'])
            print(movie['director'])
            print((movie['year']))
            print('\n')
    else:
        print("Currently No movie in the stack! :( ")


def find_movie():
    inq = input("Enter movie name: ")
    for movie in movies:
        if inq == movie['name']:
            print(movie)
    else:
        print(f"{inq} not found!")


menu()
