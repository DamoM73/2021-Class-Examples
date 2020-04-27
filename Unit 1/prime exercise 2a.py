def is_prime(candidate):
    # determines if candidate is a prime number
    dividend = 2
    while True:
        if candidate % dividend == 0:
            return False
        elif candidate - dividend == 1:
            return True
        else:
            dividend += 1

def find_next_prime(start):
    if start < 3:
        next_num = 3
    else:
        next_num = start

    while True:
        if is_prime(next_num):
            return next_num
        else:
            next_num += 1

# ----- MAIN PROGRAM -----
highest_prime = 0

while True:
    highest_prime = find_next_prime(highest_prime + 1)
    print(highest_prime)