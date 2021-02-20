myFile = open("data.txt", "r")
fileContent = myFile.read()
myFile.close()
print(fileContent)

myFile2 = open("data.txt", "w")
fileWriting = myFile2.write("Arif(edited)")
myFile2.close()
