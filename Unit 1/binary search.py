find = 11
found = False
num_list = [1,3,4,5,7,9,11,14,16]
length = len(num_list)
lower_bound = 0
upper_bound = length

while found == False:
    midpoint = (upper_bound + lower_bound) // 2
    if num_list[midpoint] == find:
        print("Found at", midpoint)
        found = True
    else:
        if list(midpoint)