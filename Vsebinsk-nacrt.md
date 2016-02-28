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
