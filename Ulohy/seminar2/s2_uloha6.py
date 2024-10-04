# Frekvenčí analýza písmen ve slově (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Frequency_analysis

def HowManyLetters(word: str) -> dict:
    word_letter_list = []
    for i in range(len(word)):
        word_letter_list.append(word[i].lower())

    word_count = {}
    punct = "!?-. +;:_"
    for i in range(len(word_letter_list)):
        if word_letter_list[i] in punct:
            pass
        elif word_letter_list[i] not in word_count:
            word_count[word_letter_list[i]] = 1
        elif word_letter_list[i] in word_count:
            word_count[word_letter_list[i]] += 1
    print(word)
    for key, value in word_count.items():
        print(f"{key}: {round((value/len(word))*100, 2)}% ({value})", end=" ")
    print()

    return word_count

HowManyLetters("aaaaa")
HowManyLetters("_Kinich_")
HowManyLetters("Janik")
HowManyLetters("der Kugelschreiber")
