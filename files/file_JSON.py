import json

with open('friends_json.txt', 'r') as file:
    file_content = json.load(file)  # reads file and turn into dictionary

print(file_content['friends'][1])

cars = [
    {'model' : 'Ford',
     'year' : '1990'
    },
    {'model' : 'Toyota',
     'year' : '1997'
    }
]

with open("json_write.txt", 'w') as file1:
    json.dump(cars, file1)


json_string = '[{"name": "Arif", "age" : 23},{"name" : "None", "age": 33}]'
jstring = json.loads(json_string)
print(jstring[0]["name"])


