"""
rezvihre
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    zefiooazefi
    """
    alpha = "éèëêàôç"
    nb="eeeeaoc"
    none = ";:'?!-, "
    table = str.maketrans(alpha, nb, none)
    print(p.lower().translate(table))
    return p.lower().translate(table) == p[::-1].lower().translate(table)

#### Fonction principale


def main():
    """
    knfoeifzeozo
    """
    # vos appels à la fonction secondaire ici

    for s in ["elle, ,","ellé","radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
