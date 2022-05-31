import re

strgs = "zab..|smrt"
score = 0


class Text:
    def __init__(self, val):
        self.val = val

    def search(self):
        test = re.search(strgs, self.val)
        if test:
            return test
        else:
            return None


while True:
    print("Skór je", score)
    txt = Text(input("Zadejte větu: "))

    if txt.search():
        score += 1
        print("Text je závadný")
    else:
        print("text je v pořádku")


"""
Objekt:
    - Kontruktor bude ukladat retezec, ktery to ma projit.
    - Metoda search() bude vyhledávat zda je v textu požadované slovo.
"""
