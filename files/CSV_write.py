file = open('csv_written.txt', 'w')

lines = int(input("Number of person(s): "))
for x in range(lines):
    try:
        name, age, university, degree = input("Enter name, age, university and degree separated by spaces per line: ").split()
        file.write(', '.join([name, age, university, degree]))
        if x != lines-1:
            file.write('\n')
    except ValueError:
        print("Invalid Input try again")
        break

file.close()
