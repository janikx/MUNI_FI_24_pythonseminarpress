# Selection sort (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Selection_sort

def NumberListSort(unsorted: list) -> list:

    for i in range(len(unsorted)):
        for j in range(len(unsorted)-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted

print(NumberListSort([1, -656, 69, 10011, 2006, -85, 99, 0, 278, 17, 5, -1, 50, 5555, -2]))
