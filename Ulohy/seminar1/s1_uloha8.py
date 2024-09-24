# Test čísla na prvočíselnost s využitím předchozí funkce

def NumberOfDividers():
    n = input("Number to check: ")
    while n.isnumeric() == False:
        n = input("Number to check: ")
        print("Write a number!")
    n = int(n)
    dividers = 0

    for i in range(1, n + 1):
        if n % i == 0:
            dividers += 1
    return dividers

def TestPrimalNumber(dividers):
    if dividers > 2:
        print(f"The number is not a primal number.")
    else:
        print(f"The number is a primal number.")

dividers = NumberOfDividers()
TestPrimalNumber(dividers)