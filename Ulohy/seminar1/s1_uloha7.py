# Vrácení počtu dělitelů daného čísla

def NumberOfDividers():
    n = input("Number to check: ")
    while n.isnumeric() == False:
        n = input("Number to check: ")
        print("Write a number!")
    n = int(n)
    nprimal = False
    dividers = 0

    for i in range(1, n + 1):
        if n % i == 0:
            dividers += 1
    print(f"Number {n} has {dividers} dividers.")

NumberOfDividers()