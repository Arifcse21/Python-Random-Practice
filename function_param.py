#!/usr/bin/env python3

cars=[
    {'make':'Ford','model':'Fiesta','mileage':23000,'fuel_consumed':460},
    {'make':'Ford','model':'Focus','mileage':17000,'fuel_consumed':350},
    {'make':'Mazda','model':'MX-5','mileage':49000,'fuel_consumed':900},
    {'make':'Mini','model':'Cooper','mileage':31000,'fuel_consumed':235}
]

def calculate_mpg( car ):
    mpg=car['mileage']/car['fuel_consumed']
    name=f"{car['make']} {car['model']}"
    print(f'{name} does {mpg} miles per gallon.')


for car in cars:
    calculate_mpg(car)


def average(sequence):
    return sum(sequence) /len(sequence)

students= [
    {'name':'Rolf','grades':(67,90,95,100)},
    {'name':'Bob','grades':(56,78,80,90)},
    {'name':'Jen','grades':(98,90,95,99)},
    {'name':'Anne','grades':(100,100,95,100)}
]

for student  in students:
    print(average(student['grades']))










