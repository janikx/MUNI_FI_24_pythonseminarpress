# Ceasarova šifra (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Caesar_cipher

def CaesarCipher(text: str, n: int) -> str:
    ciphered_text = []
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ciphered_alphabeth = []

    for i in range(0, len(text)):
        ciphered_text.append(text[i])
    
    for i in range(len(alphabeth)):
        if i < len(alphabeth)-n:
            ciphered_alphabeth.append(alphabeth[i+n])
        else:
            ciphered_alphabeth.append(alphabeth[i-(len(alphabeth)-n)])

    for i in range(0, len(ciphered_text)):
        for j in range(0, len(ciphered_alphabeth)):
            if ciphered_text[i].lower() == alphabeth[j]:
                if ciphered_text[i].isupper():
                    ciphered_text[i] = ciphered_alphabeth[j].upper()
                elif ciphered_text[i].islower():
                    ciphered_text[i] = ciphered_alphabeth[j]
                break
    ciphered_text = ("").join(ciphered_text)
    
    return ciphered_text

print(CaesarCipher("Arlecchino is a good DPS, but Navia is better.", 2)) 
print(CaesarCipher("Arlecchino is a good DPS, but Navia is better.", 4))
print(CaesarCipher("Arlecchino is a good DPS, but Navia is better.", 9))
print(CaesarCipher("Arlecchino is a good DPS, but Navia is better.", 26))
