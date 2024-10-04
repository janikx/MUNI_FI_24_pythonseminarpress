# Lineární vyhledávaní hodnoty v seznamu (Pomůcka - wiki)
# https://en.wikipedia.org/wiki/Linear_search

def numberSearch(searched_value) -> int:
    try:
        searched_value = int(searched_value)
    except ValueError:
        try:
            searched_value = float(searched_value)
        except ValueError:
            pass

    for i in range(len(listitems)):
        if searched_value == listitems[i]:
            print(f"Conformity was found on position {i} in listitems (value: {searched_value}).")
            pass
    if searched_value not in listitems:
        print(f"No conformity was found.")

searched_value = input("> Which value do you want to find?: ")
listitems = ["oko", 59, -999, "avocado", "Kinich", 1.8, "Janik", "Python", "Genshin Impact", "GYMLET"]
numberSearch(searched_value)
