import tkinter

# Privzeta minimax globina, če je nismo podali ob zagonu v ukazni vrstici
MINIMAX_PRIVZETA_GLOBINA = 3 

######################################################################
## Igra

IGRALEC_X = "X"
IGRALEC_O = "O"

NEODLOCENO = None

def nasprotnik(igralec):
    if igralec == IGRALEC_X:
        return IGRALEC_O
    else:
        return IGRALEC_X

class Igra():
    def __init__(self):
        self.polje = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.na_potezi = IGRALEC_X
        self.zgodovina = []

    def shrani_pozicijo(self):
        p = [self.polje[i][:] for i in range(3)]
        self.zgodovina.append((p, self.na_potezi))

    def razveljavi(self):
        (self.polje, self.na_potezi) = self.zgodovina.pop()

    def je_veljavna(self, i, j):
        return (self.polje[i][j] is None)

    def je_konec(self):
        if self.zmagovalec() is NEODLOCENO:
            for i in range(3):
                for j in range(3):
                    if self.polje[i][j] is None:
                        return False
            return True
        else:
            return True

    def veljavne_poteze(self):
        poteze = []
        for i in range(3):
            for j in range(3):
                if self.je_veljavna(i, j):
                    poteze.append((i,j))
        return poteze

    def povleci(self, i, j):
        if self.polje[i][j] is None:
            self.shrani_pozicijo()
            self.polje[i][j] = self.na_potezi
            self.na_potezi = nasprotnik(self.na_potezi)

    def zmagovalec(self):
        # Tabela vseh trojk, ki nastopajo v igralnem polju
        trojke = [
            # Vodoravne
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # Navpične
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # Diagonali
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]]
        for t in trojke:
            ((i1,j1),(i2,j2),(i3,j3)) = t
            p = self.polje[i1][j1]
            if p != None and self.polje[i1][j1] == self.polje[i2][j2] == self.polje[i3][j3]:
                # Našli smo zmagovalno trojko
                return (p, [t[0], t[1], t[2]])
        # Ni zmagovalca
        return NEODLOCENO

######################################################################
## Igralec clovek

class Clovek():
    def __init__(self, gui):
        self.gui = gui

    def igraj(self):
        self.gui.plosca.bind('<Button-1>', self.klik)

    def klik(self, event):
        i = event.x // 100
        j = event.y // 100
        self.gui.povleci_potezo(i, j)

######################################################################
## Igralec minimax

class Minimax():
    def __init__(self, globina):
        self.globina = globina

    def poteza(self, igra, igralec):
        return igra.veljavne_poteze[0]
        
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

        # Črte na igralnem polju
        self.plosca.create_line(100,0,100,300)
        self.plosca.create_line(200,0,200,300)
        self.plosca.create_line(0,100,300,100)
        self.plosca.create_line(0,200,300,200)

        # Seznam grafičnih elementov, ki tvorijo križce in krožce
        self.figure = []

        # Prični z izbiro igralcev
        self.izbira_igralcev()

    def izbira_igralcev(self):
        """Nastavi stanje igre na izbiranje igralcev."""
        # Zaenkrat kar preskocimo izbiro igralcev in
        # predpostavimo, da sta oba igralca človeka
        self.igralec_x = Clovek(self)
        self.igralec_o = Clovek(self)
        self.zacni_igro()

    def zacni_igro(self):
        """Nastavi stanje igre na zacetek igre."""
        self.igra = Igra()
        self.igralec_x.igraj()

    def koncaj_igro(self):
        """Nastavi stanje igre na konec igre."""
        print ("KONEC!")

    def narisi_X(self, i, j):
        x = i * 100
        y = j * 100
        self.plosca.create_line(x+5, y+5, x+95, y+95)
        self.plosca.create_line(x+95, y+5, x+5, y+95)

    def narisi_O(self, i, j):
        x = i * 100
        y = j * 100
        self.plosca.create_oval(x+5, y+5, x+95, y+95)

    def povleci_potezo(self, i, j):
        """Povleci potezo (i,j)."""
        if self.igra.je_veljavna(i, j):
            if self.igra.na_potezi == IGRALEC_X:
                self.narisi_X(i, j)
            else:
                self.narisi_O(i, j)
            self.igra.povleci(i, j)
            if self.igra.je_konec():
                self.koncaj_igro()
            else:
                if self.igra.na_potezi == IGRALEC_X:
                    self.igralec_x.igraj()
                else:
                    self.igralec_o.igraj()


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

