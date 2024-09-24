# Výpis všech sudých n přirozených čísel menších než daná hranice upper_bound

def NaturalSudeNumbers():
    upper_bound = input("Upper bound number:")
    while upper_bound.isnumeric() == False:
        upper_bound = input("Upper bound number:")
        print("Write a number!")
    upper_bound = int(upper_bound)

    for i in range (2, upper_bound + 1, 2):
        if i < upper_bound:
            print(i, end=" ")
            
NaturalSudeNumbers()