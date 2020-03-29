age = int(input("How old are you? "))
if age > 16:
    print("You are old enough to drive a car and ride a moped!")
else:
    if age == 16:
        print("You are old enough to drive a moped!")
    else:
        print("Come back when you are older!")