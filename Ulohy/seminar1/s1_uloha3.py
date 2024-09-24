# Výpis prvních how_many mocnin čísla base

def PoweredNumbers():
    base = input("Base number: ")
    power = input("Number of powered numbers: ")
    while base.isnumeric() == False or power.isnumeric() == False:
        if base.isnumeric() == False:
            base = input("Base number: ")
            print("Write a number!")
        elif power.isnumeric() == False:
            power = input("Number of powered numbers: ")
            print("Write a number!")
    base = int(base)
    power = int(power)

    print(f"> Here are {power} of powered numbers with base {base}:")
    for i in range (1, power + 1):
        if i < power + 1:
            print(f"{base} powered by {i} is {base**i}")
            
PoweredNumbers()