with open('my_file.txt', 'w') as file:
    file.write("This is a test file\n")

with open('my_file.txt', 'a') as file:
    file.write("Appended Line 1\n")
    file.write("Appended Line 2\n")
