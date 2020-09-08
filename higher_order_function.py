#! /usr/bin/env python3

operations={
    'average':lambda seq:sum(seq)/len(seq),
    'total':sum, #lambda seq:sum(seq),
    'top':max #lambda seq:max(seq)
}

students=[
    {'name':'Rolf','grades':(67,90,95,100)},
    {'name':'Bob','grades':(56,78,80,90)},
    {'name':'Jen','grades':(98,90,95.99)},
    {'name':'Anne','grades':(100,100,95,100)}
]

for student in students:
    name=student['name']
    grades=student['grades']

    print(f'student: {name}')
    operation=input("Enter 'average' or 'total' or 'top': ")
    result=operations[operation](grades)
    print(result)


