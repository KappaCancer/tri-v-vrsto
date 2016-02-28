import tkinter

class Gui():
    def __init__(self, root):
        pass


######################################################################
## Glavni program

# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

if __name__ == "__main__":
    # Naredimo glavno okno in nastavimo ime
    root = tkinter.Tk()
    root.title("Tri v vrsto")
    # Naredimo objekt razreda Gui in ga spravimo v spremenljivko,
    # sicer bo Python mislil, da je objekt neuporabljen in ga bo pobrisal
    # iz pomnilnika.
    aplikacija = Gui(root)
    # Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
    # delovati, ko okno zapremo.
    root.mainloop()

