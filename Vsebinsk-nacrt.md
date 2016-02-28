# Vsebinski načrt

## Opis aplikacije

V glavnem oknu aplikacije dva igralca igrata [tri v vrsto](https://en.wikipedia.org/wiki/Tic-tac-toe). Vsak od igralcev je lahko človek ali računalnik. Človek svoje poteze vnaša tako, da z miško klikne na polje, na katerega želi igrati.

Aplikacija je v enem od treh stanj:

1. Začetek - uporabnik izbere eno od štirih možnostih igranja:
   * človek - človek
   * človek - računalnik
   * računalnik - človek
   * računalnik - računalnik
2. Igra - med igro so v oknu naslednji podartki:
   * trenutna pozicija
   * kdo je trenutno na potezi
3. Konec igre - prikazuje zmagovalno trojico (če obstaja) in podatek o zmagovalcu.

Prehodi med stanji:

* Prehod iz začetka v igro: sproži ga uporabnik, ko izbere način igranja
* Prehod iz igre v konec igre: sproži ga uporabniški vmesnik, ko ugotovi, da je igre konec
* Prehod iz konca igre v začetek igre: uporabnik klikne na gumb "igraj še enkrat"

## Struktura programa

Program je implementiran v Pythonu 3 in sestoji iz dveh delov:

1. **Uporabniški vmesnik:** uporablja knjižnico [tkinter](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html).

2. **Računalniški igralec:** računalnik bo izbiral svoje poteze z algoritmom [minimax](https://en.wikipedia.org/wiki/Minimax). V prihodnosti ga bomo nadgradili z [alfa-beta rezanjem](https://en.wikipedia.org/wiki/Alpha–beta_pruning).

### Kako zaženemo program

Glavni program poženemo z

    python3 tictactoe.py [n]

kjer je `n` neobveen parameter, ki pove maksimalno globino za minimax.

### Razredi

Vsi razredi so v datoteki `tictactoe.py`, ker gre za zelo preprosto aplikacijo.

#### Razred `Igra`

Objekt tega razreda vsebuje trenutno stanje igre, kakor tudi njeno zgodovino. Ima
naslednje metode:

* `poteza(self,i,j)`: odigraj potezo na polju `(i,j)`, pri čemer je `i` vrstica (0, 1, 2) in `j` stolpec (0, 1, 2). Če poteza ni veljavna, prekini izvajanje programa. Objekt razreda `Igra` sam ve, kdo je na potezi.
* `razveljavi(self)`: vrni se v stanje pred zadnjo potezo, metodo lahko pokličemo večkrat, s tem se premikamo navzgor po igralnem drevesu.
* `na_potezi(self)`: Kdo je na potezi? Vrne:
    * `"X"` če je na potezi križec
    * `"O"` če je na potezi krožec
    * `None` če je igre konec
* `je_veljavna(self,i,j)`: vrne `True`, če je `(i,j)` veljavna poteza, sicer `False`
* `veljavne_poteze(self)`: vrne seznam vseh veljavnih potez
* `zmagovalec(self)`: to metodo lahko kličemo samo, če `na_potezi` vrne `None` in je igre konec. Metoda vrne:
    * `("X", lst)`, če je zmagovalec križec, `lst` je seznam dolžine tri, ki vsebuje zmagovalno trojko
    * `"(O, lst)"`, če je zmagovalec krožec, `lst` je seznam dolžine tri, ki vsebuje zmagovalno trojko
    * `None`, če je igra neodločena

#### Igralci

Razne vrste igralcev (človek, algoritem minimax, algoritem alfa-beta) predstavimo vsakega
s svojim razredom. Objekt, ki predstavlja igralca, mora imeti naslednje metode:

* `poteza(self, p, igr)`: metoda vrne potezo, ki naj jo igra igralec `igr` v dani poziciji `p`. Vhodni podatki:
    * `p`: objekt razreda `Igra`, ki opisuje trenutno stanje igre. Igralec lahko vleče poteze v igri `p`, vendar jih mora tudi razveljaviti, da je ob vrnitvi stanje igre tako, kot ob klicu.
    * `igr`: kateri igralec je na potezi, možni vrednosti sta `"X"` in `"O"`
  Izhodni podatki: metoda vrne koordinate `(i,j)` poteze, ali `None`, če ni možna nobena poteza.

##### Razred `Clovek`

Igralec je človek, potezo dobi s klikom na miško.

##### Razred `Minimax`

Igralec računalnik, ki igra z metodo minimax.

