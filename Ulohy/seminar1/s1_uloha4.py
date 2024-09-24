# Výpis prvních how_many členů Fibonacciho posloupnosti
# Jako Fibonacciho posloupnost je v matematice označována nekonečná posloupnost přirozených čísel, začínající 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … (čísla nacházející se ve Fibonacciho posloupnosti jsou někdy nazývána Fibonacciho čísla), kde každé číslo je součtem dvou předchozích.

def FibonacciRatio():
    n = input("Number: ")
    while n.isnumeric() == False:
        n = input("Number: ")
        print("Write a number!")
    n = int(n)
    an = 0
    an1 = 1
    print(an, an1, end=" ")
    for i in range (0, n + 1):
        if i < n:
            an2 = an1 + an
            print((an2), end=" ")
            an = an1
            an1 = an2

FibonacciRatio()