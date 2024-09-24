# Ciferní součet

def DigitSum():
    n = input("Number to count digits: ")
    while n.isnumeric() == False:
        n = input("Number to count digits: ")
        print("Write a number!")
    sum = 0
    
    for i in n:
        sum += int(i)
    print(f"Digit summary of {n} is {sum}.")

DigitSum()