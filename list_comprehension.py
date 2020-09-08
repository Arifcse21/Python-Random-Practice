#! /usr/bin/env python3

friend=input('Enter your friend name: ')
friends=['Rolf','Anne','Bob','Charlie']
friends_lower=[name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f'{friend.title()} is one of your friends')

