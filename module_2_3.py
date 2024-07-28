my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    numbers = my_list[i]
    i += 1
    if numbers == 0:
        continue
    elif numbers > i:
        print(numbers)
