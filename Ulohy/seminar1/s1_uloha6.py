# Test čísla na prvočíselnost pomocí postupného dělení

def TestPrimalNumber():
    n = input("Number to check: ")
    while n.isnumeric() == False:
        n = input("Number to check: ")
        print("Write a number!")
    n = int(n)
    nprimal = True

    for i in range(1, n + 1):
        if n % i == 0 and (i != 1 and i != n):
            print(f"{n} is not a primal number.")
            nprimal = False
            break
    if nprimal != False:
        print(f"{n} is a primal number.")

TestPrimalNumber()