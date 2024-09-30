# Nalezení maxima v seznamu čísel (bez použití funkce max())

def maxNumber(n_numbers: list) -> int:
    max_num = n_numbers[0]
    for i in range(1, len(n_numbers)):
        if n_numbers[i] > max_num:
            max_num = n_numbers[i]
    return max_num

num_of_nums = int(input("> How many numbers do you want to add?: "))
numbers = []
for i in range(0, num_of_nums):
    item_num = int(input("> Number: "))
    numbers.append(item_num)

print(numbers)
print(maxNumber(numbers))
