# Výpis how_many náhodně vygenerovaných čísel, jejich minimum, maximum a průměr
import random

def MaxMinMid():
    n = input("Numbers: ")
    while n.isnumeric() == False:
        n = input("Numbers: ")
        print("Write a number!")
    n = int(n)
    rannums = []

    for i in range(0, n):
        rannum = random.randint(0, 10000)
        rannums.append(rannum)
        print(rannum, end= " ")

    maxn = 0
    minn = 10000
    for i in range(0, n):
        if rannums[i] > maxn:
            maxn = rannums[i]
        if rannums[i] < minn:
            minn = rannums[i]
    avgsum = 0
    for i in range(0, n):
        avgsum = avgsum + rannums[i]
    avg = (avgsum // 2)
    print()
    print(f"Max number is {maxn}, Min number is {minn} and average is {avg}")

MaxMinMid()