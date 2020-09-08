#!/usr/bin/env python3

students=[
            {"name":"Rolf",'grade':90},
            {'name':'Bob','grade':78},
            {'name':'Jen','grade':100},
            {'name':'Anne','grade':80}]
for student in students:
    name=student['name']
    grade=student['grade']
    print(f'{name} has a grade of {grade}.')
