with open("./Unit 1/test.txt", "w") as file:
    file.write("Eli,Dixon")

with open("./Unit 1/test.txt", "r") as file:
    line = file.read()
    a_list = line.split(",")
    print(a_list)
    print(a_list[0])
    print(a_list[1])


