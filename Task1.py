try:
    file = open("sample.txt", "r")
    print("Reading File content:")
    count = 1
    for line in file:
        print("Line" + str(count) + ": " + line.strip())
        count = count + 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")