# Výpis prvních how_many přirozených čísel

def NaturalNumbers():
    n = input("Natural number:")
    while n.isnumeric() == False:
        n = input("Natural number:")
        print("Write a natural number!")
    n = int(n)

    for i in range (1, n + 1):
        if i < n:
            print(i, end=", ")
        elif i == n:
            print(i, end="")
            
NaturalNumbers()