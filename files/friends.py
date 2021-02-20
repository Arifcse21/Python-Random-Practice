friends = input("Enter three friends name. Separated by commas(no spaces, please): ").split(",")

people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()]  #white spaces like space, tab, \n get removed for line.strip()
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)
friends_nearby_file = open("friends_nearby.txt", "w")
for friend in friends_nearby_set:
    print(f'{friend} is nearby')
    friends_nearby_file.write(f'{friend}\n')

friends_nearby_file.close()


