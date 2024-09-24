# Výpočet faktoriálu (n * n-1 * n-2 * ... * 1)

def Factorial():
    n = input("Number: ")
    while n.isnumeric() == False:
        n = input("Number: ")
        print("Write a number!")
    n = int(n)

    final = 1
    for i in range(1, n + 1):
        if i <= n:
            final = final * i
    print(final)

Factorial()