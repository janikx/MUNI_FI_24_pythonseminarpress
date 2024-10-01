# Lineární vyhledávaní hodnoty v seznamu (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Linear_search

def numberSearch(n: list) -> int:
    for i in range(len(numbers)):
        if n == numbers[i]:
            print(f"Number {n} was found on position {i} in numbers (list).")
            continue

searched_number = int(input("> Which number do you want to find?: "))
numbers = []
for i in range(0, 1000):
    item_num = int(input("> Number: "))
    numbers.append(item_num)

print(numbers)
print(numberSearch(searched_number))
