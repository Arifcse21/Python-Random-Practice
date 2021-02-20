file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]    #line.strip() removes all whitespaces, tab, spaces, \n

file_write = open("non_csv.txt", 'w')

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].upper()
    degree = person_data[3].title()
    file_write.write(f"{name} is {age}, studying {degree} at {university}\n")

file_write.close()


