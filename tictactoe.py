import tkinter

######################################################################
## Igra

class Igra():
    def __init__(self):
        pass

######################################################################
## Uporabniški vmesnik

class Gui():

    def __init__(self, master):
        # Napis, ki prikazuje stanje igre
        self.napis = tkinter.StringVar(master, value="Dobrodošli v 3 x 3!")
        tkinter.Label(master, textvariable=self.napis).grid(row=0, column=0)

        # Igralno območje
        self.plosca = tkinter.Canvas(master, width=300, height=300)
        self.plosca.grid(row=1, column=0, columnspan=2)
        self.plosca.bind('<Button-1>', self.klik)

        # Crte na igralnem polju
        self.plosca.create_line(100,0,100,300)
        self.plosca.create_line(200,0,200,300)
        self.plosca.create_line(0,100,300,100)
        self.plosca.create_line(0,200,300,200)


    def klik(self, event):
        """Callback za igralno plosčo, kliče se ob kliku na ploščo."""
        print ("Klik {0}, {1}".format(event.x, event.y))
        
    def izbira_igralcev(self):
        """Nastavi stanje igre na izbiranje igralcev."""
        pass

    def zacni_igro(self):
        """Nastavi stanje igre na zacetek igre."""
        pass

    def koncaj_igro(self, zmagovalec):
        """Nastavi stanje igre na konec igre."""
        pass

    def povleci_potezo(self, i, j):
        """Povleci potezo (i,j)."""
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

