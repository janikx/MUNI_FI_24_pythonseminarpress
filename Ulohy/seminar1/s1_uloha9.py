# Výpis prvních how_many prvočísel

def PrimalNumbers():
    n = input("Number: ")
    while n.isnumeric() == False:
        n = input("Number: ")
        print("Write a number!")
    n = int(n)

    for i in range(1, n + 1):
        nprimal = True
        for z in range(1, i + 1):
            if i % z == 0 and (z != 1 and z != i):
                nprimal = False
                continue
        if nprimal == True:
            print(i, end=" ")
PrimalNumbers()