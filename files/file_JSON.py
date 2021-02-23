import json

file = open('friends_json.txt', 'r')
file_content = json.load(file)  # Reads file and turns into dict
file.close()
print(file_content)

#cars = [
#    {}
#]