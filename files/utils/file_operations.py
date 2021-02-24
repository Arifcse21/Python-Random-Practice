def file_write(data, filename):
    with open(filename, "w") as file:
        file.write(data)


def file_read(filename):
    with open(filename) as file:
        return file.read()
