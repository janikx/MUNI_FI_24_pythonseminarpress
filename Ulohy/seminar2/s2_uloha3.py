# Otočení řetězce pozpátku (bez použití metody sort() nebo funkce reversed())

def reverseString(unrev: str) -> str:
    rev = []
    for i in range(len(unrev)-1, -1, -1):
        rev.append(unrev[i])
    rev = ("").join(rev)
    return rev

string = input("> Put something in here: ")
print(reverseString(string))
