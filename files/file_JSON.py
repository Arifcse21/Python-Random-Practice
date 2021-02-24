import json

file = open('friends_json.txt', 'r')
file_content = json.load(file)  # reads file and turn into dictionary
file.close()

print(file_content['friends'][1])

cars = [
    {'model' : 'Ford',
     'year' : '1990'
    },
    {'model' : 'Toyota',
     'year' : '1997'
    }
]

file1 = open("json_write.txt", 'w')
json.dump(cars, file1)
file1.close()


json_string = '[{"name": "Arif", "age" : 23},{"name" : "None", "age": 33}]'

jstring = json.loads(json_string)
print(jstring[0]["name"])


