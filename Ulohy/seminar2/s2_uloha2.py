# Lineární vyhledávaní hodnoty v seznamu (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Linear_search

def numberSearch(n: list) -> int:
    for i in range(len(numbers)):
        if n == numbers[i]:
            print(f"Number {n} was found on position {i} in numbers (list).")
            pass

searched_number = int(input("> Which number do you want to find?: "))
numbers = []
for i in range(0, 1000):
    numbers.append(i)
<<<<<<< HEAD
    
=======

>>>>>>> 9d714743fdef27a19ea32a183ab2ce6b9fe0426b
numberSearch(searched_number)
