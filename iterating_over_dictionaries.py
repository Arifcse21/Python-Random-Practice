#! /usr/bin/env python3

friend_ages={'Rolf':25,'Anne':37,'Charlie':31,'Bob':33}

for name in friend_ages:
    print(name)

for age in friend_ages.values():
    print(age)

for name in friend_ages.keys():
    print(name)

for name,age in friend_ages.items():
    print(f'{name} is {age} years old.')
